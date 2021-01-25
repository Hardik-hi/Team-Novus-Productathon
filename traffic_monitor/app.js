const express = require("express");
const app = express();
const server = require("http").Server(app);

const io = require("socket.io")(server);

const { spawn } = require("child_process");

app.set("view engine", "ejs");

app.use(express.static("public"));

app.use(express.urlencoded({ extended: false }));

app.get("/", (req, res) => {
  res.render("traffic_management");
});

io.on("connection", (socket) => {
  console.log("Connected to the server...");

  var dataToSend;
  // spawn new child process to call the python script
  const python = spawn("python3", ["traffic_monitoring.py"]);

  python.stdout.on("data", function (data) {
    dataToSend = data.toString();

    socket.emit("change-color", dataToSend);
  });
});

const port = process.env.PORT || 8080;
server.listen(port, () => console.log(`Server running on port ${port}`));
