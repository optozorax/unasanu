const fieldSize2 = 60
const scaleFactor2 = 2

class CellularAutomaton {
  constructor(rule, width, height) {
    this.rule = rule;
    this.width = width;
    this.height = height;
    this.cells = new Array(width * height).fill(false);
    this.nextGeneration = new Array(width * height).fill(false);
    this.parseRule();
  }

  parseRule() {
    const match = this.rule.match(/B(\d*)\/S(\d*)/);

    if (!match) {
      throw new Error("Invalid rule format");
    }

    this.birthConditions = this.parseConditions(match[1]);
    this.survivalConditions = this.parseConditions(match[2]);
  }

  parseConditions(conditionString) {
    const conditionsArray = Array.from(conditionString).map(Number);
    const conditions = new Array(9).fill(false);

    conditionsArray.forEach(num => {
      if (num >= 0 && num <= 8) {
        conditions[num] = true;
      }
    });

    return conditions;
  }

  randomizeCells() {
    let percent = Math.random();
    for (let i = 0; i < this.cells.length; i++) {
      this.cells[i] = Math.random() < percent;
    }
  }

  getCell(x, y) {
    const wrappedX = (x + this.width) % this.width;
    const wrappedY = (y + this.height) % this.height;
    return this.cells[wrappedY * this.width + wrappedX];
  }

  setCell(x, y, state) {
    const wrappedX = (x + this.width) % this.width;
    const wrappedY = (y + this.height) % this.height;
    this.cells[wrappedY * this.width + wrappedX] = state;
  }

  calculateNextGeneration() {
    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        const index = y * this.width + x;
        const aliveNeighbors = this.getAliveNeighbors(x, y);
        this.nextGeneration[index] = this.applyRules(this.cells[index], aliveNeighbors);
      }
    }
    [this.cells, this.nextGeneration] = [this.nextGeneration, this.cells];
  }

  getAliveNeighbors(x, y) {
    let aliveNeighbors = 0;
    for (let yOffset = -1; yOffset <= 1; yOffset++) {
      for (let xOffset = -1; xOffset <= 1; xOffset++) {
        if (xOffset === 0 && yOffset === 0) continue;
        if (this.getCell(x + xOffset, y + yOffset)) aliveNeighbors++;
      }
    }
    return aliveNeighbors;
  }

  applyRules(currentState, aliveNeighbors) {
    if (currentState) {
      return this.survivalConditions[aliveNeighbors];
    } else {
      return this.birthConditions[aliveNeighbors];
    }
  }

  clearField() {
    this.cells.fill(false);
  }

  parsePattern(pattern, startX, startY) {
    const lines = pattern.trim().split('\n');
    
    for (let y = 0; y < lines.length; y++) {
      const line = lines[y].trim();
      
      for (let x = 0; x < line.length; x++) {
        if (line[x] === 'O') {
          this.setCell(startX + x, startY + y, true);
        }
      }
    }
  }
}

function generateRandomRule() {
  const birthConditions = generateRandomConditions();
  const survivalConditions = generateRandomConditions();
  
  const birthString = conditionsToString(birthConditions);
  const survivalString = conditionsToString(survivalConditions);
  
  return `B${birthString}/S${survivalString}`;
}

function generateRandomConditions() {
  const conditions = new Array(9).fill(false);
  const numConditions = Math.floor(Math.random() * 9) + 1;
  
  for (let i = 0; i < numConditions; i++) {
    const randomIndex = Math.floor(Math.random() * 9);
    conditions[randomIndex] = true;
  }
  
  return conditions;
}

function conditionsToString(conditions) {
  return conditions.map((condition, index) => condition ? index : "").filter(Boolean).join("");
}

function drawAutomatonOnCanvas(automaton, pixelSize, canvasId) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) {
    console.error("Canvas element not found");
    return;
  }

  const ctx = canvas.getContext("2d");
  const width = automaton.width * pixelSize;
  const height = automaton.height * pixelSize;

  canvas.width = width;
  canvas.height = height;

  for (let y = 0; y < automaton.height; y++) {
    for (let x = 0; x < automaton.width; x++) {
      const cellState = automaton.getCell(x, y);
      const color = cellState ? "black" : "white";

      ctx.fillStyle = color;
      ctx.fillRect(x * pixelSize, y * pixelSize, pixelSize, pixelSize);
    }
  }
}

function copyField(sourceAutomaton, targetAutomaton) {
  if (
    sourceAutomaton.width !== targetAutomaton.width ||
    sourceAutomaton.height !== targetAutomaton.height
  ) {
    console.error("Source and target automaton dimensions do not match");
    return;
  }

  for (let y = 0; y < sourceAutomaton.height; y++) {
    for (let x = 0; x < sourceAutomaton.width; x++) {
      const sourceCellState = sourceAutomaton.getCell(x, y);
      targetAutomaton.cells[y * targetAutomaton.width + x] = sourceCellState;
    }
  }
}

class Automatas {
  constructor() {
    let width = fieldSize2;
    let height = fieldSize2;
    this.array = [
      new CellularAutomaton("B3/S23", width, height),
      new CellularAutomaton("B36/S23", width, height),
      new CellularAutomaton("B3678/S34678", width, height),
      new CellularAutomaton("B5678/S45678", width, height),
      new CellularAutomaton("B3/S12345", width, height),
      new CellularAutomaton("B1357/S1357", width, height),
      new CellularAutomaton("B38/S238", width, height),
      new CellularAutomaton("B12345678/S1234567", width, height),
    ];

    this.setTitles();
  }

  setTitles() {
    let i = 0;
    for (let automata of this.array) {
      let title = document.getElementById("hMany" + i);
      title.textContent = automata.rule;
      i += 1;
    }
  }

  copyStateFromZeroAutomata() {
    for (let automata of this.array) {
      copyField(this.array[0], automata);
    }
  }

  randomizeCells() {
    this.array[0].randomizeCells();
    this.copyStateFromZeroAutomata();
  }

  drawEverything() {
    let i = 0;
    for (let automata of this.array) {
      drawAutomatonOnCanvas(automata, scaleFactor2, "canvasMany" + i);
      i += 1;
    }
  }

  calculateNextGeneration() {
    for (let automata of this.array) {
      automata.calculateNextGeneration();
    }
  }

  clearField() {
    for (let automata of this.array) {
      automata.clearField();
    }
  }

  setGliderGun() {
    this.clearField();

    // https://conwaylife.com/patterns/gosperglidergun.cells
    const pattern = "........................O\n......................O.O\n............OO......OO............OO\n...........O...O....OO............OO\nOO........O.....O...OO\nOO........O...O.OO....O.O\n..........O.....O.......O\n...........O...O\n............OO";

    this.array[0].parsePattern(pattern, 10, 10);

    this.copyStateFromZeroAutomata();
  }
};

let automatas = new Automatas();
automatas.setGliderGun();
automatas.drawEverything();

let calculate2 = false

const step2 = () => {
  automatas.calculateNextGeneration();
  automatas.drawEverything();
}

const intervalStep2 = () => {
  if (calculate2) {
    step2()
  }
}

let interval2 = setInterval(intervalStep2, 80)
document.querySelector('#step2').addEventListener('click', step2)
document.querySelector('#start-stop2').addEventListener('click', () => {
  calculate2 = !calculate2
})

document.querySelector('#glider2').addEventListener('click', () => {
  automatas.clearField();
  automatas.array[0].setCell(10, 10, true);
  automatas.array[0].setCell(11, 10, true);
  automatas.array[0].setCell(12, 10, true);
  automatas.array[0].setCell(12, 9, true);
  automatas.array[0].setCell(11, 8, true);

  automatas.copyStateFromZeroAutomata();

  automatas.drawEverything();
})

document.querySelector('#glidergun2').addEventListener('click', () => {
  automatas.setGliderGun();
  automatas.drawEverything();
})

document.querySelector('#random2').addEventListener('click', () => {
  automatas.randomizeCells();
  automatas.drawEverything();
})

document.querySelector('#copy2').addEventListener('click', () => {
  automatas.copyStateFromZeroAutomata();
  automatas.drawEverything();
})


document.querySelector('#randomRules2').addEventListener('click', () => {
  let i = 0;
  for (let automata of automatas.array) {
    if (i != 0) {
      automata.rule = generateRandomRule();
      automata.parseRule();
    }
    i += 1;
  }
  automatas.setTitles();
})
