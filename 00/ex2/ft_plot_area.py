#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plot_area.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/16 18:11:27 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/24 17:46:40 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plot_area() -> None:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print(f"Plot area: {area}")
