# Few-Shot Examples Documentation

## Overview

The StorytellerAgent uses **few-shot learning** to guide story generation. Each story category has a curated example that demonstrates:
- Appropriate tone and style for ages 5-10
- Story structure and pacing
- Character development
- Age-appropriate themes and vocabulary
- Narrative coherence

## Why Few-Shot Learning?

Few-shot examples help the LLM:
1. **Understand expected style**: See what a good story looks like
2. **Match category characteristics**: Learn genre-specific conventions
3. **Maintain consistency**: Produce stories that fit the category
4. **Improve quality**: Reduce hallucinations and improve coherence

## Category-Specific Examples

### ADVENTURE Category

**Example Story (Excerpt):**
```
Once upon a time, there was a brave little explorer named Maya who loved 
discovering new places. One sunny morning, Maya found a mysterious map in 
her grandmother's attic. The map showed a path to a hidden treasure in the 
nearby forest.

Maya grabbed her backpack filled with snacks and a flashlight, and set off 
on her adventure. She followed the map carefully, crossing streams and 
climbing small hills. Along the way, she met friendly animals who helped 
her find the right path.

Finally, after solving a tricky puzzle written on an old tree, Maya 
discovered the treasure: a beautiful collection of her grandmother's 
childhood memories. The real treasure was learning about her family's 
history and the joy of exploring.
```

**Key Elements Demonstrated:**
- Clear protagonist with a goal
- Journey/quest structure
- Obstacles that are age-appropriate (puzzles, not dangers)
- Discovery and learning
- Positive resolution

### FRIENDSHIP Category

**Example Story (Excerpt):**
```
Lily and Sam were best friends who did everything together. One day, a new 
student named Alex joined their class. Alex seemed shy and didn't talk to 
anyone.

Lily noticed Alex sitting alone during lunch and decided to invite them to 
join her and Sam. At first, Sam felt a little left out because Lily was 
spending time with Alex. But then Sam realized that having more friends 
meant more fun!

Together, the three friends discovered they all loved the same games and 
stories. They learned that friendship isn't about having just one friend, 
but about making room for everyone. Lily, Sam, and Alex became the best 
of friends, and they always included each other in their adventures.
```

**Key Elements Demonstrated:**
- Relationship dynamics
- Empathy and inclusion
- Conflict resolution (feeling left out)
- Growth and learning about friendship
- Positive message about inclusion

### MAGIC/FANTASY Category

**Example Story (Excerpt):**
```
In a small town where magic was hidden in everyday things, lived a young 
girl named Emma who could talk to flowers. Every morning, the flowers in 
her garden would whisper stories about the magical creatures that lived in 
the nearby woods.

One evening, a tiny fairy named Pip appeared at Emma's window, asking for 
help. The fairy's magical forest was losing its sparkle because the 
creatures had forgotten how to believe in magic.

Emma and Pip set off on a magical journey, meeting talking trees, singing 
birds, and dancing fireflies. Together, they reminded everyone that magic 
comes from believing, being kind, and seeing wonder in ordinary moments. 
The forest's sparkle returned, brighter than ever before.
```

**Key Elements Demonstrated:**
- Magical elements integrated naturally
- Wonder and imagination
- Problem-solving through belief and kindness
- Age-appropriate fantasy (not scary)
- Positive message about wonder in everyday life

### ANIMALS Category

**Example Story (Excerpt):**
```
Bunny the rabbit was the smallest animal in the meadow, but she had the 
biggest heart. All the other animals thought she was too small to help with 
important tasks, but Bunny believed she could do anything she set her mind 
to.

When the meadow's food supply started running low, all the animals worried. 
Bunny had an idea: she could reach the small spaces where berries grew that 
bigger animals couldn't access. She organized all the meadow animals to work 
together, each using their unique abilities.

Thanks to Bunny's clever thinking and teamwork, the meadow animals had plenty 
of food for the winter. Bunny learned that being small didn't mean being 
less important, and everyone learned that working together makes everyone 
stronger.
```

**Key Elements Demonstrated:**
- Animal protagonists with human-like qualities
- Overcoming limitations
- Teamwork and collaboration
- Using unique strengths
- Positive self-worth message

### PROBLEM-SOLVING Category

**Example Story (Excerpt):**
```
Jake loved building things, but his favorite toy robot had stopped working. 
He tried everything - new batteries, checking all the parts, even asking 
his parents for help. Nothing seemed to work.

Instead of giving up, Jake decided to think like a scientist. He carefully 
took the robot apart and examined each piece. He drew pictures of what he 
saw and made notes about how everything connected.

After studying the problem, Jake realized that a small wire had come loose. 
With patience and careful attention, he fixed the wire and put the robot 
back together. The robot worked perfectly! Jake learned that problems can 
be solved by being patient, observant, and not giving up.
```

**Key Elements Demonstrated:**
- Systematic problem-solving approach
- Persistence and patience
- Scientific thinking
- Learning from failure
- Achievement through effort

### EVERYDAY Category

**Example Story (Excerpt):**
```
Every morning, Maya helped her family by making her bed and setting the 
breakfast table. She loved these small routines because they made her feel 
capable and responsible.

One day, Maya's little brother was feeling sad because he couldn't tie his 
shoes. Maya remembered how patient her parents had been when teaching her, 
so she sat down with her brother and showed him step by step.

After practicing together every morning, Maya's brother learned to tie his 
shoes. He was so proud! Maya felt happy too, because she had learned that 
helping others and being patient feels wonderful. It became their special 
morning routine.
```

**Key Elements Demonstrated:**
- Relatable everyday situations
- Family relationships
- Teaching and helping
- Routine and responsibility
- Positive family dynamics

### MIXED Category

**Example Story (Excerpt):**
```
Emma loved her everyday life, but she also dreamed of magical adventures. 
One ordinary Tuesday, something extraordinary happened. While playing in 
her backyard, Emma discovered a small door that appeared in the base of an 
old oak tree.

Curious, Emma opened the door and found herself in a magical forest where 
animals could talk and flowers glowed with soft light. A friendly rabbit 
named Pip asked for her help - the forest's magic was fading because 
children had stopped believing in wonder.

Emma used her problem-solving skills from school and her kindness to help 
the forest creatures. She organized a plan to show the magic to other 
children, proving that everyday life can be full of wonder if you look for 
it. The forest's magic grew stronger, and Emma learned that adventure and 
friendship can be found anywhere.
```

**Key Elements Demonstrated:**
- Combining multiple category elements
- Bridge between ordinary and magical
- Problem-solving in fantasy context
- Friendship themes
- Message about finding wonder in everyday life

## How Examples Are Used

### In Story Generation Prompts

1. **Example Selection**: Based on the category determined by CategorizerAgent
2. **Integration**: Example is included in the prompt after the base instructions
3. **Format**: Examples are clearly labeled and formatted for the LLM
4. **Purpose**: Show the model the expected output format, style, and structure

### Example Prompt Structure

```
[Base Instructions]
[Age-Appropriateness Guidelines]
[Story Arc Guidance]
[User Request]

EXAMPLES:

Example 1:
[Category-specific example story excerpt]

Please create a complete bedtime story based on this request...
```

## Benefits of This Approach

1. **Consistency**: Stories match category expectations
2. **Quality**: Examples demonstrate high-quality storytelling
3. **Style Matching**: Tone and style appropriate for ages 5-10
4. **Structural Guidance**: Shows proper story arc implementation
5. **Reduced Hallucinations**: Clear examples reduce off-topic content

## Example Selection Criteria

Each example was chosen to:
- Be **age-appropriate** (vocabulary, themes, length)
- Demonstrate **clear story structure** (beginning, middle, end)
- Show **character development** and **positive themes**
- Match **category characteristics** accurately
- Be **engaging** and **educational**
- Use **simple, clear language** suitable for ages 5-10

## Future Enhancements

Potential improvements:
- Multiple examples per category for variety
- Dynamic example selection based on user request specifics
- Example adaptation based on story length requirements
- User feedback integration to improve example selection

