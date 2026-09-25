#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_name.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/24 17:22:55 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/24 17:46:46 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_garden_name() -> None:
    name: str = (input("Enter garden name: "))
    print(f"Garden: {name}\nStatus: Growing well!")
