#!/usr/bin/env ruby

# Accepts the first argument from the command line
input = ARGV[0]

# Regular expression to match the pattern
regex = /hbo*n|hbt+n|hbn/

# Prints matches
puts input.scan(regex).join
