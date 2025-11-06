# Storytelling System

A multi-agent AI system that generates high-quality, age-appropriate bedtime stories for children ages 5-10. The system uses specialized agents (Categorizer, Storyteller, and Judge) working together through an iterative refinement process to create engaging stories.

## Features

- **Multi-Agent Architecture**: Specialized agents for categorization, story generation, and quality evaluation
- **Iterative Refinement**: Stories are automatically improved based on judge feedback
- **Category-Specific Generation**: 7 story categories (Adventure, Friendship, Magic/Fantasy, Animals, Problem-Solving, Everyday, Mixed) with tailored prompts
- **Story Arc Structure**: Three-act narrative structure for coherent storytelling
- **5-Dimensional Evaluation**: Comprehensive quality assessment across multiple criteria
- **User Feedback Integration**: Request modifications and generate improved versions

## Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your API key:
   - Copy `.env` file
   - Replace `your_openai_api_key_here` with your actual OpenAI API key

### Usage

Run the storytelling system:
```bash
python3 main.py
```

Enter a story request when prompted, and the system will:
1. Categorize your request
2. Generate an initial story
3. Evaluate and refine the story (if needed)
4. Present the final story with quality scores

### Testing

Run the test suite to verify all components:
```bash
python3 test.py
```

## System Architecture

The system uses three specialized agents:

- **CategorizerAgent**: Classifies story requests into categories
- **StorytellerAgent**: Generates engaging stories with category-specific prompts
- **JudgeAgent**: Evaluates stories on 5 dimensions and provides feedback

See `docs/architecture.md` for detailed architecture documentation.

## Documentation

Comprehensive documentation is available in the `docs/` folder:

- **[Architecture](docs/architecture.md)** - System design and components
- **[Block Diagrams](docs/block_diagram.md)** - Visual system flow and interactions
- **[Few-Shot Examples](docs/few_shot_examples.md)** - Category-specific examples
- **[Story Arcs](docs/story_arcs.md)** - Narrative structure templates
- **[Judging System](docs/judging.md)** - Evaluation dimensions and criteria
- **[Temperature Settings](docs/temperature_settings.md)** - LLM temperature configuration
- **[Assignment Instructions](docs/instructions.md)** - Original assignment requirements

## Project Structure

```
.
├── agents/              # Agent implementations
│   ├── base_agent.py   # Base agent class
│   ├── categorizer.py  # Story categorization agent
│   ├── storyteller.py  # Story generation agent
│   └── judge.py        # Story evaluation agent
├── prompts/            # Prompt templates
│   └── prompt_templates.py
├── utils/              # Utility functions
│   ├── story_arcs.py   # Story structure templates
│   └── refinement_loop.py  # Iterative improvement
├── docs/               # Documentation
├── main.py             # Main application entry point
├── test.py             # Test suite
└── requirements.txt    # Python dependencies
```

## Key Design Decisions

- **Temperature Settings**: Different temperatures per agent (0.2 for Judge, 0.3 for Categorizer, 0.7 for Refinement, 0.8 for Storyteller)
- **Iteration Limit**: Maximum 2 refinement iterations to balance quality and efficiency
- **Quality Threshold**: 7.0/10 score threshold for triggering refinement
- **Story Arc**: Three-act structure (Beginning 25%, Middle 50%, Ending 25%)

## Example Story Requests

Try these examples:
- "A story about a brave little bunny who goes on an adventure"
- "A story about a girl named Alice and her best friend Bob, who happens to be a cat"
- "A magical story about a young wizard learning to use their powers"
- "A story about a dog who helps solve a problem in the neighborhood"

## Future Enhancements

If given 2 more hours, I would focus on:
1. Multi-judge ensemble for more reliable scoring
2. Story persistence and learning from successful examples
3. User preference learning to adapt generation parameters
4. Enhanced visualization with story arc diagrams
5. Story customization options (length, themes, characters)

## License

This project was created for the Hippocratic AI coding assignment.

