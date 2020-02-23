#!/bin/usr/env python2 
#! -*- coding: UTF-8 -*-
# Author global var :)
__AUTHOR__ = "MR-Z3R0"
import sys
import os
import random
import shutil
import importlib
import queue
#from Queue import Queue
from silentsploit.core.exceptions import *
from silentsploit.utils import *
from silentsploit.core.colors import *
from collections import Counter
APP_DIR = app_path.__path__[0]
PATH_DIR = silentsploit_path.__path__[0]
SRC_DIR = silentsploit_src.__path__[0]
printer_queue = queue.Queue()

class SilentSploit(object):
 def __init__(self):
   self._name = "\033[4mSSF\033[0m" 
   self._prompt_template = "{}{} > "
   self._base_prompt = self._prompt_template.format('', self._name)
   self.current_config = None
   self.module_prompt_template = "{} {}(\033[1;31m{}\033[0m) > " 
   self.modules = index_modules()
   self.app_dir = humanize_path(APP_DIR)
   self.counter = Counter()
   self.counter.update([module.split('.')[0] for module in self.modules])
   #Declaring the info messages
   self.__messages_info()
   # Version name
   self.version = "v1.0.5-beta-e782a8"
 @property
 def _get_config_metadata(self):
    return getattr(self.current_config,"__info__")
    
 def information(self):
    # Information message it need vars and some colors
    message = """
           =[  {YELLOW}SilentSploit {version}{clr}          ]
    + .. ..=[ {handlers} Handlers - {exploits} Exploits - {generic} Generic       ]
    + .. ..=[ {encoders} Encoders - {payloads} Payloads - {cuts} Cuts          ]
    + .. ..=[ {GREEN}Codename Author: {RED}{author}{clr}                  ]
    + .. ..=[ {YELLOW}Free silentsploit {clr}- https://t.me/S0ZS78   ]
    """
    # Returning message :)
    return message
 # Return class name
 def __get_class(self, *args, **kwargs):
    try:
      return self.current_config.__class__.__name__
    except:
      return "undefined"
 def banner(self):
    banners = []
    # Joining APP DIR WITH Logos path
    PATH = ''.join((APP_DIR, "/logos/"))
    # Walking all dirs and files from new path
    for root, dirs, files in os.walk(PATH):
       _, package, root = root.rpartition("app/logos/".replace("/", os.sep))
       root = root.replace(os.sep, ".")
       # Ignore all files starts with __ or end with .py 
       files = filter(lambda x: not x.startswith("__") and not x.endswith(".py"), files)
       banners.extend(map(lambda x: "".join((PATH, x)), files))
       banners = random.choice(banners)
       with open(banners, 'r') as file:
           banners = file.read()
           banners = banners.format(**colors)
           banners += self.information().format(version=self.version, author=__AUTHOR__, handlers=self.counter["handlers"], exploits=self.counter["exploits"], generic=self.counter["generic"], encoders=self.counter["encoders"], payloads=self.counter["payloads"], cuts=self.counter["cuts"],  **colors)
    # Returning banner will print start screen or banner command
    return banners
    
 def command_banner(self, *args, **kwargs):
    print(self.banner())
    
 def _prompt_helper(self):
    if self.current_config:
      try:
         return self.module_prompt_template.format(self._name, self.__get_class(), self._get_config_metadata["Name"])
      except (AttributeError, KeyError):
         return self.module_prompt_template.format(self._name, self.__get_class(), "UnnamedModule")
    else:
      return self._base_prompt
      
 def _getproxys(self):
  """
   Function return a proxy
   in case proxys in attributes is defined
   it will return a random proxy
   
   : return proxies
  """
  try:
    res = reqs.get('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt', headers={'User-Agent':'Mozilla/5.0'})
    lines = res.text.split("\n")
    proxies = random.choice(lines)
    return proxies
  except:
    print_error("Cant get proxies")
 def get_command_handler(self, command):
   try:
      command_handler = getattr(self, "command_{}".format(command))
   except AttributeError:
      raise SilentSploitException("Unknown command: '{}'".format(command))
   return command_handler
   
 def parse_line(self, line):
  """ Split line into command and argument.

   :param line: line to parse
   :return: (command, argument, named_arguments)
   RouterSploit credits :3
  """
  kwargs = dict()
  command, _, arg = line.strip().partition(" ")
  args = arg.strip().split()
  for word in args:
    if '=' in word:
       (key, value) = word.split('=', 1)
       kwargs[key.lower()] = value
       arg = arg.replace(word, '')
  return command, ' '.join(arg.split()), kwargs
  
 def __messages_info(self):
  self.global_help = """
    Core commands
    ==============\n 
    Command                  Description
    --------                 ------------
    help                     display this help menu
    use <module>             load a module or checker
    back                     back the current menu
    exit                     close the console
    banner                   print an awesome banner
    info                     show info about developer and framework
    exec <command> <args>    execute a command from shell
    run                      run a given module using command "use"
    show info|options|all    show information, modules and options      
    unset <value>            unset local value was set
    load plugin|framework    (For a future update :) )
    set  <value>             set value from current module
  """
  self.info_menu = """\033[0m
  SilentSploit is another  framework (?
  Our framework is an multi purpose embedded framework
  We'be developing explotation, intrusion and more. 
  Account checkers, BruteForce tools, exploits,  payloads and more!\n
  [Disclaimer] 
  Our framework was developed for controlled envoriments, the
  misuse that is done with it is not our responsibility.
  Code snippets from \033[1;31mRoutersploit\033[0m.
  --> Only for pentesting <--\n
  [Developer] 
  {YELLOW}Mr-Z3r0{clr}, creator and developer of The framework.
  I love hacking and programming, hacking you since 2018-2020
  Creator and admin of TheDeathWing.\n	
  [Sponsors]
  Not sponsors. Want u be one?
  """
  
 @config_required
 def command_back(self, *args, **kwargs):
   self.current_config = None
   
 def start(self):
  os.system('cls' if os.name == 'nt' else 'clear')
  print(self.banner())
  printer_queue.join()
  while True:
    try:
      command, args, kwargs = self.parse_line(input(self._prompt_helper()))
      if not command:
        continue
      command_handler = self.get_command_handler(command)
      command_handler(args, **kwargs)
    except SilentSploitException as Err:
      print_error(Err)
    except (EOFError, KeyboardInterrupt, SystemExit):
      print_error("Ups, silentsploit was stopped.")
      break
    except Exception as Err:
      print_error(Err)
    finally:
      printer_queue.join()
      
 def _check_file(self, fname):
    try:
       f = open(fname)
       return True
    except IOError:
       return False
       
 @config_required
 def command_unset(self, *args, **kwargs):
    key, _, value = args[0].partition(" ")
    if key in self.current_config.options:
        setattr(self.current_config, key, "")
        self.current_config.exploit_attributes[key][0] = ""
        print_success("{} was unset".format(key))
    else:
       print_error("Can't unset {}".format(key))
       
 @config_required 
 def command_set(self, *args, **kwargs):
    key, _, value = args[0].partition(" ")
    if key in self.current_config.options and value != "":
        setattr(self.current_config, key, value)
        self.current_config.exploit_attributes[key][0] = value
        if kwargs.get("glob", False):
          GLOBAL_OPTS[key] = value
        print_success("{} => {}".format(key, value))
    else:
     print_error("You can't set option '{}'.\n"
    "Available options: {}".format(key, self.current_config.options))
    
 @config_required
 def _show_info(self, *args, **kwargs):
    pprint_dict_in_order(
     self._get_config_metadata,
      ("Name", "Description", "Authors", "LastModified"),
    )
    print_info()
    
 @config_required
 def get_opts(self, *args):
    """ Generator returning module's advanced Option attributes (option_name, option_value, option_description)
 
    :param args: Option names
    :return:
    """
    for opt_key in args:
      try:
         opt_description = self.current_config.exploit_attributes[opt_key][1]
         opt_display_value = self.current_config.exploit_attributes[opt_key][0]
      except (KeyError, AttributeError):
         pass
      else:
         yield opt_key, opt_display_value, opt_description
 
 @config_required
 def get_opts_adv(self, *args):
    """ Generator returning module's advanced Option attributes (option_name, option_value, option_description)
 
    :param args: Option names
    :return:
    """
    for opt_key in args:
       try:
          opt_description = self.current_config.exploit_attributes[opt_key][1]
          opt_display_value = self.current_config.exploit_attributes[opt_key][0]
       except (KeyError, AttributeError):
          pass
       else:
          yield opt_key, opt_display_value, opt_description
          
 @config_required
 def _show_options(self, *args, **kwargs):
     target_names = ["target", "port", "ssl", "rhost", "rport", "lhost", "lport"]
     target_opts = [opt for opt in self.current_config.options if opt in target_names]
     module_opts = [opt for opt in self.current_config.options if opt not in target_opts]
     headers = ("Name", "Current settings", "Description")
     
     print_info("\nTarget options:")
     print_table(headers, *self.get_opts(*target_opts))
 
     if module_opts:
        print_info("\nModule options:")
        print_table(headers, *self.get_opts(*module_opts))
    
     print_info()
 def __show_options(self, root=''):
     for module in [module for module in self.modules if module.startswith(root)]:
        print_info(module.replace('.', os.sep))
        
 def _show_payloads(self, *args, **kwargs):
     self.__show_options('payloads')
     
 def _show_bruteforce(self, *args, **kwargs):
     self.__show_options('bruteforce')
     
 def _show_all(self, *args, **kwargs):
     self.__show_options()
     
 def _show_cuts(self, *args, **kwargs):
     self.__show_options('cuts')
     
 def _show_encoders(self, *args, **kwargs):
     self.__show_options('encoders')
     
 def _show_generic(self, *args, **kwargs):
     self.__show_options('generic')
     
 def command_show(self, *args, **kwargs):
     sub_command = args[0]
     try:
        getattr(self, "_show_{}".format(sub_command))(*args, **kwargs)
     except AttributeError:
        print_error("show subcommand doesn't exists")
        
 def command_info(self, *args, **kwargs):
    print(self.info_menu.format(**colors))
    
 def _help_menu(self, option):
   msg = [
       'What? i didnt understand. Try help.',
       'That command dont appears to exists.',
       'Sorry but i dont know this command.',
       'Maybe you need help, try command \'help\'.'
   ]
   print("\033[1;31m%s\033[0m"%(random.choice(msg)))
   return
   
 def command_exec(self, *args, **kwargs):
    os.system(args[0])
    
 def copy_file(self, fname, *args, **kwargs):
   #print os.path.isfile(fname)
   filen = os.path.basename(fname)
   try:
      print_status("Copying file...")
      shutil.copyfile(fname, self.configdir+filen)
      print_success("The file {fname} was copied successful.".format(fname=fname))
   except shutil.Error as e:
      print_error("Unable to copy file. %s" % e)
      
 def check_extension(self, file, *args, **kwargs):
    file = PATH_DIR+"/"+file
    if file.endswith(self.filextension):
      try:
        f = open(file)
        return True
      except IOError:
        print_error("File not accessible")
    else:
      print_error("File extension is not allowed.")
        
 @config_required
 def command_run(self, *args, **kwargs):
   print_status("Running module...")
   try:
      self.current_config.run()
   except KeyboardInterrupt:
      print_error("Accion cancelled by user")
   except Exception as Err:
      print_error("An error ocurred: `{}`".format(Err))
   
 def command_help(self, *args, **kwargs):
    print_info(self.global_help)
    
 def command_use(self, config_file):
   config_file = pythonize_path(config_file)
   config_file = ".".join(("silentsploit","modules", config_file))
   try:
      self.current_config = import_config(config_file)()
   except SilentSploitException as err:
      print_error(str(err))
 def command_exit(self, *args, **kwargs):
   raise EOFError
   