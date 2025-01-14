#!/usr/bin/env ruby

# Accepts the first argument from the command line
input = ARGV[0]

# Regular expression to capture sender, receiver, and flags
regex = /from:([^ ]+).*to:([^ ]+).*flags:([^\]]+)/

# Match and capture the groups
matches = input.match(regex)

# If matches are found, print in the desired format
if matches
  sender = matches[1]
  receiver = matches[2]
  flags = matches[3]
  puts "#{sender},#{receiver},#{flags}"
end
