const fieldSize = 100
const scaleFactor = 3

let field = []
for (let y = 0; y < fieldSize; y++) {
  field[y] = []
  for (let x = 0; x < fieldSize; x++) {
    field[y][x] = Math.random() * 100 > 65
  }
}

const getNeighbors = (x, y, field) => {
  let prevX = x - 1
  if (prevX < 0) {
    prevX = field[0].length - 1
  }

  let nextX = x + 1
  if (nextX === field[0].length) {
    nextX = 0
  }

  let prevY = y - 1
  if (prevY < 0) {
    prevY = field.length - 1
  }

  let nextY = y + 1
  if (nextY === field.length) {
    nextY = 0
  }

  return [
    field[prevY][prevX],
    field[prevY][x],
    field[prevY][nextX],
    field[y][prevX],
    // field[y][x], That's the cell itself - we don't need this.
    field[y][nextX],
    field[nextY][prevX],
    field[nextY][x],
    field[nextY][nextX],
  ]
}

const getDeadOrAlive = (x, y, field) => {
  const neighbors = getNeighbors(x, y, field)
  const numberOfAliveNeighbors = neighbors.filter(Boolean).length

  // Cell is alive
  if (field[y][x]) {
    if (numberOfAliveNeighbors < 2 || numberOfAliveNeighbors > 3) {
      // Cell dies
      return false
    }

    // Cell stays alive
    return true
  }

  // Cell is dead
  if (numberOfAliveNeighbors === 3) {
    // Cell becomes alive
    return true
  }

  // Cell stays dead
  return false
}

const drawField = field => {
  const canvas = document.querySelector('#canvas')
  const context = canvas.getContext('2d')

  context.fillStyle = '#fff'
  context.fillRect(0, 0, fieldSize * scaleFactor, fieldSize * scaleFactor);

  context.fillStyle = '#000'

  field.forEach((row, y) => row.forEach((cell, x) => {
    if (cell) {
      context.fillRect(x * scaleFactor, y * scaleFactor, scaleFactor, scaleFactor)
    }
  }))
}

drawField(field)

let calculate = false

const step = () => {
  let prev = field
  field = prev.map((row, y) => row.map((_, x) => {
    return getDeadOrAlive(x, y, prev)
  }))

  drawField(field)
}

const intervalStep = () => {
  if (calculate) {
    step()
  }
}

let interval = setInterval(intervalStep, 80)

document.querySelector('#step').addEventListener('click', step)

document.querySelector('#start-stop').addEventListener('click', () => {
  calculate = !calculate
})

document.querySelector('#reset').addEventListener('click', () => {
  for (let y = 0; y < fieldSize; y++) {
    for (let x = 0; x < fieldSize; x++) {
      field[y][x] = false
    }
  }

  drawField(field)
})

document.querySelector('#glider').addEventListener('click', () => {
  for (let y = 0; y < fieldSize; y++) {
    for (let x = 0; x < fieldSize; x++) {
      field[y][x] = false
    }
  }

  field[20][20] = true
  field[20][21] = true
  field[20][22] = true
  field[19][22] = true
  field[18][21] = true

  drawField(field)
})

document.querySelector('#random').addEventListener('click', () => {
  for (let y = 0; y < fieldSize; y++) {
    for (let x = 0; x < fieldSize; x++) {
      field[y][x] = Math.random() * 100 > 65
    }
  }

  drawField(field)
})

let drawing = false

document.querySelector('#canvas').addEventListener('mousedown', event => {
  drawing = true
})
document.querySelector('#canvas').addEventListener('mouseup', event => {
  drawing = false
})

document.querySelector('#canvas').addEventListener('mousemove', event => {
  if (drawing) {
    const x = Math.floor(event.offsetX / scaleFactor)
    const y = Math.floor(event.offsetY / scaleFactor)

    field[y][x] = !field[y][x]

    drawField(field)
  }
})
