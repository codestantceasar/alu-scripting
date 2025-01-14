#!/usr/bin/env ruby

# Accepts the first argument from the command line
input = ARGV[0]

# Regular expression to match capital letters
regex = /[A-Z]+/

# Join and print only the capital letters found in the input
puts input.scan(regex).join
