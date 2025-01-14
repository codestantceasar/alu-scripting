#!/usr/bin/env ruby
# This script matches strings like htn, hbtn, hbbtn, hbbbtn
puts ARGV[0].scan(/hbt{0,}n/).join
