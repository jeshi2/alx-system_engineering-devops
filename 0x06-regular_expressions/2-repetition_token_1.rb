#!/usr/bin/env ruby

input = ARGV[0]

matches = input.scan(/School/i)
puts matches.join
