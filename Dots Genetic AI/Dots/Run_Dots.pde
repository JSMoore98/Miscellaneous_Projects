//Program based on: https://www.youtube.com/watch?v=BOZfhUcNiqk&list=PLwNzDmqBL87UGJqApM-Fcxy5OxXEPZIGq&index=44&t=0s

Population test;
PVector goal  = new PVector(400, 10);


void setup() {
  test = new Population(1000);//create a new population with 1000 members
}

  void settings() {
    size(800, 800); //size of the window
  }

void draw() { 
  background(255);

  //draw goal
  fill(255, 0, 0);
  ellipse(goal.x, goal.y, 10, 10);

  //draw obstacle(s)
  fill(0, 0, 255);

  rect(0, 300, 600, 10);
  
  fill(0, 0, 255);

  rect(200, 500, 800, 10);


  if (test.allDotsDead()) {
    //genetic algorithm
    test.calculateFitness();
    test.naturalSelection();
    test.mutateDemBabies();
  } else {
    //if any of the dots are still alive then update and then show them

    test.update();
    test.show();
  }
}
