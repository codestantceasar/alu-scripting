#!/usr/bin/env ruby

# Accepts the first argument from the command line
input = ARGV[0]

# Regular expression to match the 10-digit phone number
regex = /^\s*\d{3}[-\s]?\d{3}[-\s]?\d{4}\s*$/

# Prints matches
puts input.scan(regex).join
