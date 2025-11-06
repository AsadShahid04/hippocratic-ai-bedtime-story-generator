# System Architecture Documentation

## Overview

The Storytelling System is a multi-agent architecture designed to create high-quality, age-appropriate bedtime stories for children ages 5-10. The system uses three specialized agents working together through an iterative refinement process.

## System Components

### Core Agents

1. **CategorizerAgent** - Classifies story requests into specific categories
2. **StorytellerAgent** - Generates complete bedtime stories
3. **JudgeAgent** - Evaluates story quality across multiple dimensions

### Supporting Infrastructure

- **BaseAgent** - Base class providing common LLM interaction functionality
- **RefinementLoop** - Orchestrates iterative story improvement
- **StoryArc** - Provides story structure templates
- **PromptTemplate** - Manages prompt formatting and templates

## System Flow

```
User Request
    │
    ▼
┌─────────────────────┐
│  CategorizerAgent   │ ← Classifies request into 7 categories
│  (Temperature: 0.3) │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ StorytellerAgent    │ ← Generates initial story
│ (Temperature: 0.8) │    with category-specific prompts
└──────────┬──────────┘    and story arc structure
           │
           ▼
┌─────────────────────┐
│   JudgeAgent        │ ← Evaluates on 5 dimensions
│ (Temperature: 0.2)  │    provides structured feedback
└──────────┬──────────┘
           │
           ▼
    ┌─────────────┐
    │ Score < 7.0? │
    └──────┬───────┘
           │
      ┌────┴────┐
      │         │
     Yes       No
      │         │
      ▼         ▼
┌──────────┐  ┌──────────────┐
│ Refine   │  │ Final Story  │
│ Story    │  │ (Complete)   │
└────┬─────┘  └──────────────┘
     │
     │ (Max 2 iterations)
     ▼
┌─────────────────────┐
│ StorytellerAgent    │ ← Generates improved version
│ (Temperature: 0.7) │    based on judge feedback
└──────────┬──────────┘
           │
           ▼
     (Loop back to Judge)
```

## Agent Responsibilities

### CategorizerAgent

- **Purpose**: Understand user intent and classify story type
- **Input**: User's story request (free text)
- **Output**: Category name + explanation
- **Categories**: ADVENTURE, FRIENDSHIP, MAGIC/FANTASY, ANIMALS, PROBLEM-SOLVING, EVERYDAY, MIXED
- **Temperature**: 0.3 (lower for consistent categorization)

### StorytellerAgent

- **Purpose**: Generate complete, engaging bedtime stories
- **Input**: User request + category + story arc guidance
- **Output**: Complete story text (500-1000 words)
- **Features**:
  - Category-specific few-shot examples
  - Story arc structure (three-act or five-part)
  - Age-appropriateness guidelines
- **Temperature**: 0.8 (higher for creative storytelling)
- **Refinement Temperature**: 0.7 (slightly lower for focused improvements)

### JudgeAgent

- **Purpose**: Evaluate story quality and provide actionable feedback
- **Input**: Generated story text
- **Output**: Structured evaluation with scores and suggestions
- **Evaluation Dimensions**: 5 key areas (see `judging.md`)
- **Temperature**: 0.2 (very low for consistent, reasoned evaluations)

## Refinement Loop

The `RefinementLoop` class manages the iterative improvement process:

1. **Initial Generation**: Storyteller generates first draft
2. **Evaluation**: Judge evaluates on all 5 dimensions
3. **Decision**: Check if any dimension scores below threshold (default: 7.0)
4. **Refinement**: If needed, generate improved version based on feedback
5. **Iteration Limit**: Maximum 2 iterations to balance quality and API costs

### Evaluation History Tracking

The refinement loop maintains a complete history:

- Each iteration's story version
- Full evaluation for each version
- Dimension scores and feedback for each iteration
- Final assessment of whether refinement occurred

This allows analysis of improvement patterns and debugging of the refinement process.

## Design Decisions

### Temperature Settings

- **Categorizer (0.3)**: Lower temperature ensures consistent categorization
- **Storyteller (0.8)**: Higher temperature enables creative, engaging narratives
- **Judge (0.2)**: Very low temperature for consistent, reasoned evaluations
- **Refinement (0.7)**: Slightly reduced from initial generation to focus improvements

### Iteration Limit

Maximum 2 iterations chosen to:

- Balance story quality improvement
- Control API costs
- Avoid over-refinement that might lose original intent
- Maintain reasonable response times

### Story Arc Structure

Default: Three-act structure (Beginning, Middle, Ending)

- Act 1 (25%): Introduction and setup
- Act 2 (50%): Challenges and complications
- Act 3 (25%): Resolution and learning

Alternative: Five-part structure available for more complex narratives.

## File Structure

```
agents/
  ├── base_agent.py      # Base class for all agents
  ├── categorizer.py     # Story categorization agent
  ├── storyteller.py     # Story generation agent
  └── judge.py           # Story evaluation agent

utils/
  ├── story_arcs.py      # Story structure templates
  └── refinement_loop.py # Iterative improvement orchestration

prompts/
  └── prompt_templates.py # Prompt formatting utilities

main.py                  # Main application entry point
test.py                  # Test suite
```

## API Integration

All agents use OpenAI's `gpt-3.5-turbo` model (as specified in requirements). The BaseAgent class handles:

- API key management via `.env` file
- Consistent API calling interface
- Error handling for missing credentials

## Age-Appropriateness

The system embeds age-appropriateness guidelines throughout:

- Vocabulary constraints (simple, clear words)
- Sentence length limits (mostly under 15-20 words)
- Theme restrictions (positive, educational, no scary content)
- Story length targets (500-1000 words)

These guidelines are passed to all story generation prompts and used in evaluation.
