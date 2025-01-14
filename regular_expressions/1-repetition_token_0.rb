#!/usr/bin/env ruby


def match_pattern(input)  
  # Regular expression to match the specified patterns  
  regex = /^hbt+n$/  
  if input.match(regex)  
    puts "Match"  
  else  
    puts "No Match"  
  end  
end  

# Get the input from command line arguments  
if ARGV.length != 1  
  puts "Please provide exactly one argument."  
else  
  match_pattern(ARGV[0])  
end
