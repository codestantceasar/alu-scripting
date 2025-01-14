#!/usr/bin/env ruby

# Accept the first argument from the command line
input = ARGV[0]

# Regular expression to match the pattern with 1 to 6 't's
regex = /^hbt{1,5}n$/

# Check if the input matches the pattern and print the result
if input.match(regex)
  puts input
end
