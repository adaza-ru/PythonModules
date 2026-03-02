#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/16 18:17:07 by adaza-ru            #+#    #+#            #
#   Updated: 2026/02/16 18:25:42 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_water_reminder():
    days = int(input("Enter plant age in days: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
