# System Block Diagram

## High-Level System Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    STORYTELLING SYSTEM                          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ User Request
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         MAIN ORCHESTRATOR                       │
│                    (StorytellingSystem Class)                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  CATEGORIZER │    │ STORYTELLER  │    │    JUDGE     │
│    AGENT     │    │    AGENT     │    │    AGENT     │
└──────────────┘    └──────────────┘    └──────────────┘
        │                     │                     │
        │                     │                     │
        ▼                     ▼                     ▼
   Category +          Story Text          Evaluation +
   Explanation                              Feedback
```

## Detailed Component Interactions

```
┌─────────────────────────────────────────────────────────────────────┐
│                           USER INPUT                                 │
│              "A story about a brave bunny adventure"                 │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│                    STEP 1: CATEGORIZATION                           │
├──────────────────────────────────────────────────────────────────────┤
│  CategorizerAgent                                                   │
│  ├─ Input: User request text                                       │
│  ├─ Prompt: Category classification prompt                          │
│  ├─ Temperature: 0.3 (low for consistency)                          │
│  ├─ Processing: LLM analyzes request                                │
│  └─ Output: Category (e.g., "ADVENTURE") + explanation             │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│                  STEP 2: STORY GENERATION                           │
├──────────────────────────────────────────────────────────────────────┤
│  StorytellerAgent                                                    │
│  ├─ Input: User request + Category                                   │
│  ├─ Prompt Components:                                               │
│  │   ├─ Age-appropriateness guidelines                              │
│  │   ├─ Category-specific few-shot example                          │
│  │   ├─ Story arc structure (three-act)                              │
│  │   └─ User request                                                 │
│  ├─ Temperature: 0.8 (high for creativity)                          │
│  ├─ Processing: LLM generates complete story                         │
│  └─ Output: Initial story text (500-1000 words)                     │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│                    STEP 3: EVALUATION                                │
├──────────────────────────────────────────────────────────────────────┤
│  JudgeAgent                                                          │
│  ├─ Input: Generated story text                                      │
│  ├─ Prompt Components:                                               │
│  │   ├─ Age-appropriateness guidelines                              │
│  │   ├─ Evaluation rubric (5 dimensions)                            │
│  │   └─ Story text                                                   │
│  ├─ Temperature: 0.2 (very low for consistency)                     │
│  ├─ Processing: LLM evaluates on 5 dimensions                        │
│  └─ Output: Structured evaluation                                    │
│      ├─ Dimension scores (1-10)                                       │
│      ├─ Reasoning for each score                                     │
│      ├─ Actionable suggestions                                       │
│      └─ Overall assessment                                            │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Score < 7.0?        │
                    └──────────┬────────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                   Yes                   No
                    │                     │
                    ▼                     ▼
        ┌───────────────────┐   ┌──────────────────┐
        │  REFINEMENT LOOP  │   │   FINAL STORY    │
        └───────────────────┘   └──────────────────┘
                    │
                    │ (Max 2 iterations)
                    ▼
┌──────────────────────────────────────────────────────────────────────┐
│                    STEP 4: REFINEMENT                               │
├──────────────────────────────────────────────────────────────────────┤
│  RefinementLoop                                                      │
│  ├─ Input: Story + Evaluation feedback                              │
│  ├─ Processing:                                                     │
│  │   ├─ Generate refinement instructions                            │
│  │   ├─ Storyteller generates improved version                        │
│  │   │   (Temperature: 0.7 for focused improvement)                 │
│  │   └─ Judge re-evaluates                                          │
│  ├─ History Tracking:                                               │
│  │   ├─ Iteration count                                              │
│  │   ├─ All story versions                                           │
│  │   ├─ All evaluations per iteration                                │
│  │   └─ Improvement tracking                                         │
│  └─ Output: Final refined story + evaluation                        │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│                        FINAL OUTPUT                                  │
├──────────────────────────────────────────────────────────────────────┤
│  • Complete story text                                               │
│  • Category and explanation                                          │
│  • Quality evaluation scores                                          │
│  • Refinement history (if applicable)                                │
└──────────────────────────────────────────────────────────────────────┘
```

## Data Flow Diagram

```
User Request (Text)
        │
        ├─→ [CategorizerAgent] ──→ Category + Explanation
        │         │
        │         └─→ Category Info
        │
        ├─→ [StorytellerAgent] ──→ Initial Story
        │         │
        │         ├─→ Age Guidelines
        │         ├─→ Story Arc Template
        │         ├─→ Category Example (Few-shot)
        │         └─→ User Request
        │
        └─→ [JudgeAgent] ──→ Evaluation
                │
                ├─→ Age Guidelines
                ├─→ Evaluation Rubric
                └─→ Story Text
                        │
                        ├─→ Dimension Scores
                        ├─→ Reasoning
                        ├─→ Suggestions
                        └─→ Overall Assessment
                                │
                                └─→ [Decision Logic]
                                        │
                                        ├─→ Score >= 7.0? ──→ Final Story
                                        │
                                        └─→ Score < 7.0? ──→ Refinement Loop
                                                                │
                                                                └─→ [RefinementLoop]
                                                                        │
                                                                        ├─→ Refined Story
                                                                        ├─→ Re-evaluation
                                                                        └─→ History Tracking
```

## Component Dependencies

```
BaseAgent (Base Class)
    │
    ├─→ CategorizerAgent
    │       └─→ PromptTemplate
    │
    ├─→ StorytellerAgent
    │       ├─→ PromptTemplate
    │       ├─→ StoryArc
    │       └─→ get_age_guidelines()
    │
    └─→ JudgeAgent
            ├─→ PromptTemplate
            └─→ get_age_guidelines()

RefinementLoop
    ├─→ StorytellerAgent (for refinement)
    ├─→ JudgeAgent (for evaluation)
    ├─→ PromptTemplate (for refinement prompts)
    └─→ get_age_guidelines()

StorytellingSystem (Main Orchestrator)
    ├─→ CategorizerAgent
    ├─→ StorytellerAgent
    ├─→ JudgeAgent
    └─→ RefinementLoop
```

## Prompt Flow Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    PROMPT CONSTRUCTION                       │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Categorizer  │   │ Storyteller  │   │    Judge     │
│   Prompts    │   │   Prompts    │   │   Prompts    │
└──────────────┘   └──────────────┘   └──────────────┘
        │                   │                   │
        │                   │                   │
        ▼                   ▼                   ▼
   Base Prompt       Base Prompt        Base Prompt
        │                   │                   │
        │                   │                   │
        ▼                   ▼                   ▼
   Variables         Variables +         Variables +
   (request)         Examples +          Guidelines +
                     Arc Guidance        Rubric
```

## Temperature Settings Flow

```
┌─────────────────────────────────────────────────────────┐
│              TEMPERATURE SELECTION                      │
└─────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
  Low (0.2-0.3)      Medium (0.7)        High (0.8)
        │                   │                   │
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│   Judge      │   │ Refinement   │   │ Storyteller  │
│  (Consistent)│   │ (Focused)    │   │ (Creative)   │
└──────────────┘   └──────────────┘   └──────────────┘
```

