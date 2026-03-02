#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/16 19:46:18 by adaza-ru            #+#    #+#            #
#   Updated: 2026/02/16 19:52:45 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative():
    n = int(input("Days until harvest: "))
    for day in range(1, n + 1):
        print(f"Day {day}")
    print("Harvest time!")
