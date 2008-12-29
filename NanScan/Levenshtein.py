#   Copyright (C) 2008 by Albert Cervera i Areny
#   albert@nan-tic.com
#
#   This program is free software; you can redistribute it and/or modify 
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or 
#   (at your option) any later version. 
#
#   This program is distributed in the hope that it will be useful, 
#   but WITHOUT ANY WARRANTY; without even the implied warranty of 
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License 
#   along with this program; if not, write to the
#   Free Software Foundation, Inc.,
#   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA. 


# TODO: If available, wrap levenshtein C implementation

class Levenshtein:

	@staticmethod
	def levenshtein( text1, text2 ):
		# Levenshtein distance if one string is empty, is the
		# length of the other string, len(text) inserts.
		if len(text1) == 0:
			return len(text2)
		if len(text2) == 0:
			return len(text1)

		# Build array of len(text1) * len(text2)
		d = [ [0] * len(text2) ] * len(text1)

		for i in range(len(text1)):
			d[i][0] = i

		for j in range(len(text2)):
			d[0][j] = j

		for i in range(len(text1)-1): 
			for j in range(len(text2)-1):
				ip = i+1
				jp = j+1
				if text1[ip] == text2[jp]:
					cost = 0
				else:
					cost = 1

				d[ip][jp] = min( 
					d[ip-1][jp] + 1,      # deletion
					d[ip][jp-1] + 1,      # insertion
					d[ip-1][jp-1] + cost  # substitution
				)
		return d[len(text1)-1][len(text2)-1]

if __name__ == '__main__':
	print Levenshtein.levenshtein( 'abc', 'abc' )
	print Levenshtein.levenshtein( 'abcabc', 'abc' )
	print Levenshtein.levenshtein( 'abcdef', 'abc' )
	print Levenshtein.levenshtein( 'abcdef', 'bcd' )
	print Levenshtein.levenshtein( 'bcdef', 'abc' )
	for x in range(10000):
		Levenshtein.levenshtein( 'text de la plantilla', 'text llarg que pot ser del document que tractem actualment' )