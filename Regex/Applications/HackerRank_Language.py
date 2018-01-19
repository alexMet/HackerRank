import re

n = int(input())
p = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC".split(":")

for _ in range(0, n):
    ret = re.match(r"^\d\d\d\d\d (.*)$", input())
    
    if str(ret.group(1)) in p:
        print ("VALID")
    else:
        print ("INVALID")
