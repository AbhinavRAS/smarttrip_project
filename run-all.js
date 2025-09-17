const { exec } = require("child_process");

// Function to execute a command and log its output
function runCommand(command, description) {
    console.log(`\n=== Running: ${description} ===`);
    exec(command, (err, stdout, stderr) => {
        if (err) {
            console.error(`Error running ${description}: ${err.message}`);
            return;
        }
        if (stdout) console.log(stdout);
        if (stderr) console.error(stderr);
    });
}

// Run Node.js file
runCommand("node index.js", "Node.js Script (index.js)");

// Run Python scripts (if any)
runCommand("python main.py", "Python Script (main.py)"); // Replace 'main.py' with the actual Python file name

// Run Docker Compose (if applicable)
runCommand("docker compose up --build", "Docker Services");

// Add more commands as needed for other files or services