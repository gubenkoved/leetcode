//go:build ignore

package main

import (
	"fmt"
	"regexp"
	"strconv"
)

type Spreadsheet struct {
	cells [][]int
}

func Constructor(rows int) Spreadsheet {
	cells := [][]int{}

	for row := 0; row < rows+1; row++ {
		cells = append(cells, make([]int, 26))
	}

	return Spreadsheet{
		cells: cells,
	}
}

func ToIndexes(cell string) (int, int) {
	col := int(cell[0] - 'A')
	row, _ := strconv.ParseInt(cell[1:], 10, 32)
	return int(row), col
}

func (this *Spreadsheet) SetCell(cell string, value int) {
	row, col := ToIndexes(cell)
	this.cells[row][col] = value
}

func (this *Spreadsheet) ResetCell(cell string) {
	row, col := ToIndexes(cell)
	this.cells[row][col] = 0
}

func (this *Spreadsheet) GetCell(cell string) int {
	row, col := ToIndexes(cell)
	return this.cells[row][col]
}

var formulaRegexp = regexp.MustCompile(`^=([A-Z0-9]+)\+([A-Z0-9]+)$`)

func Resolve(spreadsheet *Spreadsheet, ref string) int {
	if ref[0] >= 'A' && ref[0] <= 'Z' {
		return spreadsheet.GetCell(ref)
	}
	value, _ := strconv.ParseInt(ref, 10, 32)
	return int(value)
}

func (this *Spreadsheet) GetValue(formula string) int {
	groups := formulaRegexp.FindStringSubmatch(formula)
	return Resolve(this, groups[1]) + Resolve(this, groups[2])
}

func main() {
	ss := Constructor(10)
	ss.SetCell("A1", 1)
	ss.SetCell("A2", 5)
	fmt.Println(ss.GetValue("=A1+A2"))
}
