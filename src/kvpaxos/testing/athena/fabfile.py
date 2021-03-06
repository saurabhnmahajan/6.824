from __future__ import with_statement
from fabric.api import run, env, local
from fabric.context_managers import cd
from fabric.contrib.console import confirm

# Must provide Athena password, then possibly provide Github username 
# and password for Github source code access.

env.hosts = ['athena.dialup.mit.edu']
env.user = 'dhubble'

def git_pull():
	run("git clone git@github.com:dghubble/6.824-labs.git && ls")
	position_for_test()

def git_update():
	run("cd 6.824-labs && git pull origin master")
	position_for_test()

def position_for_test():
	run("cd 6.824-labs/src && export GOPATH=$HOME/6.824-labs && cd kvpaxos && go test -i")

def simple_test():
	run("cd 6.824-labs/src && export GOPATH=$HOME/6.824-labs && cd kvpaxos && go test -i && go test > debug.log 2> error.log")

def medium_round():
	run("cd 6.824-labs/src && export GOPATH=$HOME/6.824-labs && cd kvpaxos && go test -i && bash repeat_test.sh > test/test.log")