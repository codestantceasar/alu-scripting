#!/usr/bin/env ruby

# Accepts the first argument from the command line
input = ARGV[0]

# Regular expression to match the pattern
regex = /hb?t?n/

# Prints matches
puts input.scan(regex).join
