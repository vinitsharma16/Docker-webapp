import webbrowser as wb
import pyttsx3

pyttsx3.speak("Hello")
print()
print("WELCOME TO MY INTELLIGENCE WORLD".center(125))                    
# engine.runAndWait()
pyttsx3.speak("I am your voice assistant")
pyttsx3.speak("How can i assist you...?")


while True:
  print()
  print("\t \t \t Tell me your requirements")
  ch=input()
  
  if("date" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=date")
    pyttsx3.speak("showing date")
  elif("calendar" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=cal")
    pyttsx3.speak("showing calendar")
  elif("IP" in ch )or ("ip address" in ch) or ("address" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=ifconfig")
    pyttsx3.speak("showing IP address")
  elif("active ports" in ch) or ("ports" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=netstat%20-tnlp")
    pyttsx3.speak("showing active ports")
  elif("amount" in ch) or ("disc" in ch) and ("space" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=df%20-h")
    pyttsx3.speak("showing amount of disc space")
  elif("status" in ch) or ("webserver" in ch) and ("apache" in ch) or ("httpd" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=systemctl%20status%20httpd")
    pyttsx3.speak("apache webserver is running")
  elif("state of selinux" in ch) or ("selinux" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=getenforce")
    pyttsx3.speak("SElinux is permissive")
  elif("yum" in ch) or ("module" in ch) and ("list" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=yum%20module%20list")
    pyttsx3.speak("Here is the long list of modules")
  elif("package" in ch) or ("firefox" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=yum%20whatprovides%20firefox")
    pyttsx3.speak("Here is the package name of firefox")
  elif("ping" in ch) or ("google" in ch) and ("server" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=ping%20-c%205%208.8.8.8")
    pyttsx3.speak("Server is Ping able")
  
  #install package
  elif("yum" in ch) or ("module" in ch) and ("install" in ch):
    packagename=input("Enter package name to install: ")
    wb.open(f"http://192.168.43.202/cgi-bin/newtask.py?x=yum%20install%20{packagename}%20-y") #check format
    pyttsx3.speak("Package is installed")
  
  ##find file
  elif("find" in ch) or ("search" in ch) and ("file" in ch):
    filename=input("Enter file name to search: ")
    dirpath=input("Enter the location: ")
    
    # wb.open(f"http://192.168.43.202/cgi-bin/newtask.py?x=find%20./{dirpath}%20-name%20{filename}")  #if command not worked try 
    wb.open(f"http://192.168.43.202/cgi-bin/newtask.py?x=find%20{dirpath}%20-name%20{filename}") #check format
    #pyttsx3.speak("Package is installed")
    pyttsx3.speak("File Found")
  
  ##set cronjobs
  elif("set" in ch) or ("create" in ch) and ("cronjobs" in ch):
    command=input("Enter command to run in every two minutes: ")
    filename=input("Enter the filename to execute: ")
    commandpass=f"cat; | echo */2 * * * * {command} {filename}"
    # wb.open(f"http://192.168.43.202/cgi-bin/newtask.py?x=find%20./{dirpath}%20-name%20{filename}")  #if command not worked try 
    wb.open(f"http://192.168.43.202/cgi-bin/newtask.py?x=crontab%20-l%20|%20{commandpass}|%20crontab%20-") #check format
    #pyttsx3.speak("Package is installed")
    pyttsx3.speak("cronjob set")
  
  elif ("How" in ch) and ("you can" in ch) or ("help me" in ch):
    pyttsx3.speak("i can help you in following ways")
    print()
    print("!! I can help you in following ways !!".center(126))
    pyttsx3.speak("such as basic linux commands")
    print()
    print(" * Basic Linux Commands".center(126))
    pyttsx3.speak("Basic Networking")
    print()
    print(" * Basic Networking".center(126))
    pyttsx3.speak("Create User and Restrict User for Specific Program")
    print()
    print(" * Create User and Restrict User for Specific Program".center(126))
    pyttsx3.speak("Configuration of Docker")
    print()
    print(" * Configuration of Docker".center(126))
    print()
  elif("start service" in ch) or ("start docker service") and ("service") in ch:
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=systemctl%20start%20docker%20")
    pyttsx3.speak("starting docker service....")
  elif("verify docker" in ch) and ("installed" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=rpm%20-q%20docker-ce")
    pyttsx3.speak("Now docker is present in your linux server....")
  elif("how many" in ch) and ("docker containers" in ch) or ("containers" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=docker%20ps")
    pyttsx3.speak("There is no docker containers")
  elif("how many" in ch) and ("docker images" in ch) or ("images" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=docker%20images")
    pyttsx3.speak("There are so many images")
  elif("pull" in ch) or ("wordpress" in ch) and ("image" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=docker%20pull%20wordpress")
    pyttsx3.speak("word press image is successfully pulled")
  elif("launch" in ch) and ("docker container" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=docker%20run%20-dit%20wordpress")
    pyttsx3.speak("word press container is successfully launched")
  elif("verify" in ch) and ("docker container" in ch) or ("container launched" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=docker%20ps")
    pyttsx3.speak("wordpress container is running....")
  elif("list" in ch) or ("Cgi" in ch) or ("bin" in ch) :
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=ls")
    pyttsx3.speak("these are the files present in CGI BIN...")
  elif("create" in ch) or ("directory" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=mkdir%20/namenode")
    pyttsx3.speak("directory created")
  elif("SDK" in ch) or ("python library" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=pip3%20install%20boto3")
    pyttsx3.speak("boto three is already satisfied")
  elif ("lv" in ch) or ("logical volume" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=sudo%20lvdisplay")
    pyttsx3.speak("Here is the detail of your logical volume in current Volume Group...")
  elif ("vg" in ch) or ("volume group" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=sudo%20vgdisplay")
    pyttsx3.speak("Here is the detail of your Volume Group...")
  elif ("file system" in ch) or ("fs" in ch) or ("fstab" in ch):
    wb.open("http://192.168.43.202/cgi-bin/newtask.py?x=cat%20/etc/fstab%20|%20grep%20/dev")
    pyttsx3.speak("It is the file system of Linux Server")
  elif ("exit" in ch) or ("quit" in ch) or ("bye" in ch):
    pyttsx3.speak("see you soon,, have a nice day...!!!")
    break
  else:
    print("Please Try Again")
