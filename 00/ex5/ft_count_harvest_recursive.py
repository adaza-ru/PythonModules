#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/16 19:53:33 by adaza-ru            #+#    #+#            #
#   Updated: 2026/02/16 19:56:46 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))

    def count_recursive(day):
        if day > n:
            return
        print(f"Day {day}")
        count_recursive(day + 1)

    count_recursive(1)
    print("Harvest time!")
