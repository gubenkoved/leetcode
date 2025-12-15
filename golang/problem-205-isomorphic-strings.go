//go:build ignore

package main

func isIsomorphic(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	m := map[byte]byte{}
	m2 := map[byte]byte{}

	for idx := 0; idx < len(s); idx++ {
		sc := s[idx]
		tc := t[idx]

		mappedInto, isMapped := m[sc]

		if isMapped {
			if mappedInto != tc {
				return false
			}
		} else {
			// not mapped
			m[sc] = tc
			m2[tc] = sc
		}
	}

	return len(m) == len(m2)
}
