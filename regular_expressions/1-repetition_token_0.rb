#!/usr/bin/env ruby


#!/usr/bin/env ruby

# Check if an argument is passed
if ARGV.length != 1
  puts "Usage: ./match_pattern.rb <string>"
  exit 1
end

# Input string
input = ARGV[0]

# Regular expression to match the pattern
regex = /^hb(tt*)n$/

# Check if the input matches the pattern
if input.match?(regex)
  puts input
end
