from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sentinelbackend.utils import hash_file
import os
import datetime

from sentinelbackend.sqlalchemy_declarative import Base, Blacklist, badIP, scheduledFiles, badProcess

engine = create_engine('sqlite:////tmp/test.db')

def loadsession():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


if os.name != 'nt':
    import iptc


def getbadIphealth(ip):
    session = loadsession()
    if ip == 0:
        return 0
    result = list(session.query(badIP).filter_by(ip=ip))
    if len(result) > 0:
        return 6 + int((result.count % 10) / 5) if result.count > 5 else result.count
    else:
        return 0


def addToBlacklist(ip, port):
    user = Blacklist(ip=ip, port=port)
    session = loadsession()
    try:
        session.add(user)
        session.commit()
        if port != '*':
            command = ("iptables -A INPUT -p tcp --sport {} -s {} -j DROP").format(str(port), str(ip))
            if os.name == 'nt':
                command = "netsh advfirewall firewall add rule name=IPblock dir=in protocol=tcp remoteip={} localport={} action=block".format(ip, port)
                print(command)
            os.system(command)
            return "blocked"
        else:
            if os.name == 'nt':
                command = "netsh advfirewall firewall add rule name=IPblock dir=in protocol=tcp remoteip={} action=block".format(ip)
                print(command)
                os.system(command)
                return "blocked"
            rule = iptc.Rule()
            rule.protocol = 0
            rule.src = str(ip)
            target = iptc.Target(rule, "DROP")
            rule.target = target
            chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
            chain.insert_rule(rule)
        return "blocked"
    except sqlalchemy.exc.IntegrityError:
        return "ip {} is already blocked on {} port".format(ip, port if port != '*' else "all")


def removeFromBlacklist(ip, port):
    session = loadsession()
    if os.name == 'nt':
        user = Blacklist.query.filter_by(ip=ip).filter_by(port=port)
        user.delete()
        session.commit()
        command = "netsh advfirewall firewall delete rule name=IPblock dir=in protocol=tcp remoteip={} localport={}".format(ip, port)
        if port=='*':
            command = "netsh advfirewall firewall delete rule name=IPblock dir=in protocol=tcp remoteip={}".format(ip)
        os.system(command)
        return "unblocked"
    if port != '*':
        user = Blacklist.query.filter_by(ip=ip).filter_by(port=port)
        check = 0 if len(list(user)) == 0 else 1
        if check == 1:
            command = ("iptables -D INPUT -p tcp --sport {} -s {} -j DROP").format(str(port), str(ip))
            os.system(command)
            user.delete()
            session.commit()
            return "unblocked"
        else:
            return "no such rule present"
    else:
        blockedIPlist = Blacklist.query.filter_by(ip = ip)
        for blackList in blockedIPlist:
            if blackList.port == '*':
                rule = iptc.Rule()
                rule.protocol = 0
                rule.src = str(ip)
                target = iptc.Target(rule, "DROP")
                rule.target = target
                chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
                chain.delete_rule(rule)
            else:
                command = ("iptables -D INPUT -p tcp --sport {} -s {} -j DROP").format(str(blackList.port), str(blackList.ip))
                os.system(command)
        blockedIPlist.delete()
        session.commit()
        return "unblocked"

def getRules():
    session = loadsession()
    return list(map(lambda x: {
        "ip": x.ip,
        "port": x.port
    }, session.query(Blacklist).all()))


def getScheduledFiles():
    return list(map(lambda x: {
        "file": x.file,
        "hash": x.hash,
        "time": x.time,
        "user": x.user
    }, scheduledFiles.query.all()))


def addScheduledFile(filepath, hash, user="Devansh"):
    session = loadsession()
    print(str(datetime.datetime.now()), user)
    newFile = scheduledFiles(file=filepath, hash=hash, time=str(datetime.datetime.now()), user=user)
    session.add(newFile)
    session.commit()

def removeFileFromScheduled(filepath):
    session = loadsession()
    file = scheduledFiles.query.filter_by(file=filepath)
    file.delete()
    session.commit()

def badIPdetected(ip):
    session = loadsession()
    oldIp = badIP.query.filter_by(ip=ip)
    # print(list(oldIp)[0])
    if oldIp is None or len(list(oldIp)) == 0:
        newIp = badIP(ip=ip, count=1)
        session.add(newIp)
        session.commit()
    else:
        ip = oldIp.first()
        ip.count = ip.count + 1
        session.commit()
        pass

# db.drop_all()

# db.create_all()
# addToBlascklist()
# removeFromBlacklist()
# badIPdetected("12.12.12.12")