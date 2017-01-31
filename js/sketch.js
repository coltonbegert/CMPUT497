
// // Position Variables
// var x = 5;
// var y = 5;
//
// // Speed - Velocity
// var vx = 1;
// var vy = 1;
//
// // Acceleration
// var ax = 1;
// var ay = 1;
//
// var vMultiplier = 0.007;
// var bMultiplier = 0.6;
// import Math;
var x1 = 10;
var y1 = 10;
var x2 = 10;
var y2 = 10;
// var node1;
var node1;
var node2;
var connected=0;
var total=0;
var SIZE = 1000;
function setup() {


    createCanvas(1000, 1000);
    fill(0);
    node1 = new node();
    node2 = new node();
}

function draw() {


    // vx1 = 1;
    // vy1 = 0;
    // vx2 = 0;
    // vy2 = 1;
    //
    // x1 += vx1;
    // y1 += vy1;
    // x2 += vx2;
    // y2 += vy2;
    //
    // // node();
    background(255);
    noFill();
    rect(0,0,1000,1000);
    fill(0);
    node1.show();
    node2.show();
    // line(node1.y, node1.x, node2.y, node2.x);
    distance(node1, node2);
    var n = Math.round(((connected *100) / total) * 100) / 100 + "%";
    textSize(16);
    text(n,25,25);


    // string s = n.toString() + "%";

    // node1.update();
    node1.bounce();

    // node2.update();
    node2.bounce();



    // // x = x+1;
    // // ballMove();
    // ellipse(x1, y1, 30, 30);
    // ellipse(x2, y2, 30, 30);
}

function node() {
    this.x = 100;
    this.y= -1;
    this.vx= 1;
    this.vy =1;
    this.show = function() {
        ellipse(this.y,this.x,10,10);
    }
    this.update = function() {
        this.x += this.vx;
        this.y += this.vy;
        if (this.x > 1000) {
            this.vx = -random(5);
            this.vy = 10 - random(5);
        }
        if (this.y > 1000) {
            this.vx = 5 - random(10);
            this.vy = -random(5);
        }
        if (this.x <=0) {
            this.vx = random(5);
            this.vy = 5 - random(10);
        }
        if (this.y <= 0) {
            this.vx = 5 - random(10);
            this.vy = random(5);
        }
    }
    this.bounce = function() {
        this.x += 5*this.vx;
        this.y += 5*this.vy;
        if(this.x <= 0) {
            this.vx = random();
            this.vy = 1 - (2*(random()));
        }
        if (this.x >= SIZE) {
            this.vx = -random();
            this.vy = 1 - (2*(random()));
        }
        if(this.y <= 0) {
            this.vx = 1 - (2*(random()));
            this.vy = random();
        }
        if (this.y >= SIZE) {
            this.vx = 1 - (2*(random()));
            this.vy = -random();
        }
        // print(this.vx);
        // println(this.vy);
    }
}

function distance(n1, n2) {
    x2 = pow((n1.x-n2.x), 2);
    y2 = pow((n1.y-n2.y), 2);
    x2y2 = x2 + y2;
    dist = sqrt(x2y2);
    total +=1;
    if (dist < 250) {
        connected +=1;
        // var c = color(255,0,0);
        var c = color('red');
        // fill(c);  // Use 'c' as fill color
        // noStroke();
        stroke(c);
        strokeWeight(2);
        line(n1.y, n1.x, n2.y, n2.x);
        stroke(0);
        // fill(0);
    }
    // line(n1.y, n1.x, n2.y, n2.x);
}
