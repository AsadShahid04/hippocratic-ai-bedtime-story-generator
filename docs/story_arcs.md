# Story Arc Templates Documentation

## Overview

The system uses structured story arc templates to ensure generated stories have proper narrative structure. Story arcs provide a framework that guides the LLM to create stories with clear progression, satisfying development, and appropriate pacing for children ages 5-10.

## Why Story Arcs?

Story arcs ensure:
1. **Narrative Coherence**: Stories have clear beginning, middle, and end
2. **Proper Pacing**: Appropriate distribution of story elements
3. **Character Development**: Characters face challenges and grow
4. **Satisfying Endings**: Stories resolve properly
5. **Educational Value**: Stories teach through structure and resolution

## Three-Act Structure (Default)

The system uses a **three-act structure** as the default template, which is ideal for children's bedtime stories due to its simplicity and clarity.

### Act 1: Beginning (25% of story)

**Purpose**: Establish the world, characters, and initial situation

**Key Elements**:
- Who is the main character?
- Where does the story take place?
- What does the character want or need?
- What is their everyday life like?

**Percentage**: 25% of total story length

**Example Structure**:
```
Once upon a time, there was a [character] who [daily life]. 
Every day, [character] would [routine]. But one day, 
[character] wanted [goal/desire].
```

### Act 2: Middle (50% of story)

**Purpose**: Present challenges and complications

**Key Elements**:
- What problem or challenge does the character face?
- How do they try to solve it?
- What obstacles get in their way?
- What happens when they try different solutions?

**Percentage**: 50% of total story length (the longest section)

**Example Structure**:
```
[Character] decided to [action]. But [obstacle 1]. 
So [character] tried [solution 1]. That didn't work because [reason]. 
Then [character] tried [solution 2]. This time [result]...
```

### Act 3: Ending (25% of story)

**Purpose**: Resolve the problem and show character growth

**Key Elements**:
- How is the problem finally solved?
- What did the character learn?
- How are things different now?
- What is the happy ending or resolution?

**Percentage**: 25% of total story length

**Example Structure**:
```
Finally, [character] realized [insight]. With [new approach], 
[character] [solution]. Now [character] learned [lesson], 
and [positive outcome]. The end.
```

## Five-Part Structure (Alternative)

For more complex narratives, the system also supports a **five-part structure**:

### 1. Exposition (20%)
- Introduction of characters and setting
- Establishment of normal world

### 2. Rising Action (25%)
- Introduction of conflict or challenge
- Building tension

### 3. Climax (20%)
- The most exciting moment
- Biggest challenge or turning point

### 4. Falling Action (20%)
- Resolution of the conflict
- Consequences and outcomes

### 5. Resolution (15%)
- Final resolution
- Character growth and lessons learned

## Implementation in Code

### StoryArc Class

The `StoryArc` class in `utils/story_arcs.py` provides:

```python
StoryArc.get_arc_template("three_act")  # Returns structure dictionary
StoryArc.format_arc_guidance("three_act")  # Returns formatted prompt text
```

### Usage in Story Generation

The StorytellerAgent uses story arcs by:

1. **Selecting Arc Type**: Default is "three_act", can be "five_part"
2. **Formatting Guidance**: Converting template to prompt-friendly text
3. **Including in Prompt**: Adding arc guidance to generation prompts
4. **Guiding Structure**: LLM uses guidance to structure the story

### Example Prompt Integration

```
[Age-appropriateness guidelines]

Use a three-act story structure:

Beginning (25% of story):
Introduce characters and setting. Show the normal world and what 
the main character wants.
Key elements to include:
- Who is the main character?
- Where does the story take place?
...

Middle (50% of story):
The character faces challenges and tries to solve problems. 
Things get complicated.
...

Ending (25% of story):
The problem is solved, and the character learns something or grows.
...
```

## Why Three-Act for Children?

### Simplicity
- Easy for children to follow
- Clear progression they can understand
- Predictable structure that builds confidence

### Engagement
- Quick setup (25%) gets to action fast
- Long middle (50%) maintains interest
- Satisfying resolution (25%) provides closure

### Educational Value
- Teaches narrative structure
- Shows cause and effect
- Demonstrates problem-solving

### Age-Appropriate
- Not too complex for ages 5-10
- Matches typical bedtime story length
- Allows for character development within time constraints

## Story Arc Benefits in Our System

### For Story Generation
- **Guides LLM**: Clear structure prevents rambling
- **Ensures Completion**: Template ensures story has proper ending
- **Maintains Pacing**: Percentage guidelines keep pacing appropriate
- **Improves Quality**: Structured stories are more coherent

### For Evaluation
- **Judging Criteria**: Judge can evaluate structure adherence
- **Coherence Check**: Arc structure helps judge assess narrative flow
- **Character Development**: Arc ensures character growth is present

### For Refinement
- **Targeted Improvements**: Judge can suggest improvements to specific acts
- **Structure Validation**: Can check if story follows arc properly
- **Pacing Adjustments**: Can suggest lengthening/shortening specific acts

## Story Length Guidelines

With story arcs:
- **Total Length**: 500-1000 words (target)
- **Act 1 (Beginning)**: ~125-250 words
- **Act 2 (Middle)**: ~250-500 words
- **Act 3 (Ending)**: ~125-250 words

This ensures:
- Complete narrative in bedtime story timeframe
- Appropriate attention span for ages 5-10
- Satisfying story with proper development

## Customization Options

The system allows for:
- **Arc Type Selection**: Choose three-act or five-part
- **Percentage Adjustments**: Can modify act percentages if needed
- **Element Customization**: Can add category-specific arc elements
- **Dynamic Adaptation**: Could adjust based on story category

## Future Enhancements

Potential improvements:
- Category-specific arc variations
- User-selected arc types
- Dynamic arc adjustment based on story length
- Arc adherence scoring in evaluation
- Visual story arc diagrams for users

