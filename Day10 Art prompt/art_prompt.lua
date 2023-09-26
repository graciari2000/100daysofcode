-- Import the required libraries
local random = require("random")
local table = require("table")

-- Define the list of possible prompts
local prompts = {
    "Create a painting of a cat in a surrealist landscape.",
  "Draw a picture of a dog playing fetch in the park.",
  "Make a sketch of a person sitting in a cafe.",
  "Paint a picture of a cityscape at night.",
  "Draw a picture of a flower in a vase."
}

-- Generate a random prompt
local prompt = prompts[random.randint(1, #prompts)]

-- Print the prompt to the console
print(prompt)