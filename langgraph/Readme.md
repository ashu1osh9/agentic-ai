LangGraph ek framework hai jo LLM agents ko graph ke form mein design karne ke liye use hota hai.


Normal LangChain mein flow linear hota hai:

Prompt -> LLM -> Output


Lekin LangGraph mein flow graph ki tarah hota hai:

        ┌─────────┐
        │  Start  │
        └────┬────┘
             │
             ▼
      ┌────────────┐
      │ Call LLM   │
      └────┬───────┘
           │
           ▼
      ┌────────────┐
      │ Use Tool ? │
      └───┬────┬───┘
          │    │
        Yes    No
          │    │
          ▼    ▼
   ┌────────┐  End
   │ Tool   │
   └────┬───┘
        │
        ▼
    Call LLM