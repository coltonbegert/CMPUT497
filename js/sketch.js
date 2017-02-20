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
var inRange;
var currentTime = 0;
var nextColl = -1;
function setup() {


    createCanvas(1000, 1000);
    fill(0);
    node1 = new node();
    node2 = new node();
}

function draw() {
    currentTime ++;


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
    time = ttotrans(node1, node2);
    text(currentTime, 25, 75);
    if (time > 0) {
        nextColl = currentTime + time;
    }
    if (inRange) {
        nextColl = -1;
    }
    if (nextColl >= currentTime) {
        fill(0,0,255);
    } else {
        fill(0);
    }
    // if (time <= 0) {
    //     if (inRange = false) {
    //         inRange = true;
    //     }
    //     fill(0,0,255);
    // } else {
    //     if (inRange) {
    //
    //     }
    //     fill(0);
    // }
    text(time, 25, 50);
    fill(0);
    // if (time) {
    //     // background(0);
    // } else {
    //     // background(255);
    //     text("no collison", 25, 50);
    // }
    // console.log(time);
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
        inRange = true;
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
    } else {
        inRange = false;
    }
    // line(n1.y, n1.x, n2.y, n2.x);
}
function closestpointonline( lx1, ly1, lx2, ly2, x0, y0){
    this.test = 10;
    A1 = ly2 - ly1;
    B1 = lx1 - lx2;
    C1 = (ly2 - ly1)*lx1 + (lx1 - lx2)*ly1;
    C2 = -B1*x0 + A1*y0;
    det = A1*A1 - -B1*B1;
    cx = 0;
    cy = 0;
    if(det != 0){
        cx = ((A1*C1 - B1*C2)/det);
        cy = ((A1*C2 - -B1*C1)/det);
     }  else{
     cx = x0;
     cy = y0;
     }
     this.x = cx;
     this.y = cy;
    //  return new Point(cx, cy);
}

function ttotrans(point1, point2) {


    // d = new closestpointonline(point1.x, point1.y, point1.x + point1.vx, point1.y + point1.vy, point2.x, point2.y);
    // // console.log(d.cx, d.cy);
    // closestdistsq = pow((point2.x - d.x), 2) + pow((point2.y - d.y), 2);
    // backdist = Math.sqrt(Math.pow(250, 2) - closestdistsq);
    // // movementvectorlength = Math.sqrt(Math.pow(point1.vx, 2) + Math.pow(point1.vy, 2));
    // v = sqrt(pow((point1.vx - point2.vx), 2) + pow((point1.vy - point2.vy), 2))
    // time = backdist / v;
    // console.log(time);
    // if(closestdistsq <= 250){
    //     // a collision has occurred
    //     return 1;
    //     console.log("collision happens");
    // }else{
    //     // no collision has occurred
    //     return 0;
    // }
    // c_x = d.x - backdist * (point1.vx / movementvectorlength);
    // c_y = d.y - backdist * (point1.vy / movementvectorlength);



    // printf("here ttotrans\n");
    vxt = point1.vx - point2.vx;
    vyt = point1.vy - point2.vy;
    l = sqrt(pow((point1.x - point2.x), 2) + pow((point1.y - point2.y), 2))

    x0 = point1.x;
    y0 = point1.y;

    x1 = point2.x;
    y1 = point2.y;

    x2 = point2.x * point2.vx;
    y2 = point2.y * point2.vy;

    d = abs(((x2-x1) * (y1-y0)) - ((x1-x0) * (y2 - y1)))/sqrt(pow((x2-x1), 2) + pow((y2-y1), 2));
    d1 = sqrt(pow((point1.x-point2.x), 2) + pow((point1.y - point2.y), 2) - pow(d,2) );
    d2 = sqrt(pow(250,2) - pow(d, 2));
    v = sqrt(pow(vxt,2) + pow(vyt, 2));
    time = (d1 - d2) / v;
    // h = sqrt(pow(d, 2) + l) - sqrt(pow(250, 2) - pow(d, 2));
    // t = h/(sqrt(pow(vxt,2) + pow(vyt, 2)));
    if (d > 250) {
        return NaN;
    } else {
        return time;

    }
    // console.log("distance" +d);
    // console.log("time: " + t)

    // tcpa = (vxt*point1.x - vxt*point2.x + vyt*point1.y - vyt*point2.y)/(vxt*point1.vx - vxt*point2.vx + vyt*point1.vy - vyt*point2.vy);

    // if (isnan(tcpa)) {
    //     /* code */
    //     // printf("hello\n");
    //     return -1;
    // }
    // double curDist = distance(point1, point2);
    // printf("current Distance: %f\n", curDist);
    // if (curDist < 250) {
    //     //calc time to exit
    // }

    // root = sqrt(pow(point1.x + point1.vx*tcpa + point2.x + point2.vx*tcpa,2) + pow(point1.y + point1.vy*tcpa + point2.y + point2.vy*tcpa,2));
    // printf("init:: x1: %f, y1: %f, x2: %f, y2: %f,",point1.x, point1.y,  point2.x,  point2.y);
    // printf("vx1: %f, vy1: %f, vx2: %f, vy2: %f\n",point1.vx, point1.vy,  point2.vx,  point2.vy);
    // printf("vx1: %f, vx2: %f, vy1: %f, vy2: %f\n",point1.vx, point1.vy,  point2.vx,  point2.vy);
    // if (isnan(root)) return -1;
    // if ()
    // return root;
    // if (inRange) {
    //     return 250 + root;
    // } else {
    //     if (root > 250) {
    //         return -1;
    //     } else {
    //         return 250 - root;
    //     }
    // }
}
