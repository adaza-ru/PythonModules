#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/16 18:11:27 by adaza-ru            #+#    #+#            #
#   Updated: 2026/02/16 18:14:32 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_total():
    harvest1 = int(input("Day 1 harvest: "))
    harvest2 = int(input("Day 2 harvest: "))
    harvest3 = int(input("Day 3 harvest: "))
    total_harvest = harvest1 + harvest2 + harvest3
    print(f"Total harvest: {total_harvest}")
