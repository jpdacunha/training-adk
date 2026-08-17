"""
Model configuration demonstration showing factual vs creative optimization.
Demonstrates ADK's generate_content_config with different settings.
"""


from google.adk.agents import LlmAgent
from google.genai import types


# Agent 1: Optimized for Factual Data Extraction
# Uses low temperature for consistency, strict safety for accuracy

factual_agent = LlmAgent(

    model="gemini-2.5-flash", # Flash is sufficient for extraction
    name="data_extractor",
    description="Extracts factual information with high consistency",
    instruction="""You are a precise data extractor.

    Extract facts exactly as stated. Do not:

    - Add information not present in the input

    - Make assumptions or inferences

    - Use creative language
    Be accurate, concise, and deterministic.""",

    generate_content_config=types.GenerateContentConfig(

        # Controls randomness: lower values make responses more predictable, while
        # higher values allow more variation. 0.1 is close to deterministic, which
        # is useful when the same input should produce a consistent extraction.
        temperature=0.1, 
       
        # Limits the generated answer to 500 tokens. This is enough for the facts
        # this agent extracts while preventing unnecessarily long responses.
        max_output_tokens=500,

        # Keeps only the most likely tokens whose cumulative probability reaches
        # 0.8. This reduces unusual wording and supports reliable fact extraction.
        top_p=0.8,

        # Considers at most the 10 most likely next tokens. The low value narrows
        # the choices further, complementing the low temperature and top_p value.
        top_k=10,

        safety_settings=[
            types.SafetySetting(
                # Applies this rule to potentially dangerous content. The setting
                # is explicit so the agent does not rely only on model defaults.
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                # Blocks content rated low risk or higher, prioritizing a cautious
                # behavior for an agent intended to return factual information.
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
            )
        ]

    )

)

# Agent 2: Optimized for Creative Brainstorming
# Uses high temperature for creativity, Pro model for better ideas

creative_agent = LlmAgent(

    model="gemini-3.1-pro-preview", # Pro for superior creativity
    name="creative_brainstormer",
    description="Generates creative ideas and explores possibilities",
    instruction="""You are a creative brainstorming partner.

    Generate innovative, diverse, and imaginative ideas. Feel free to:

    - Think outside the box

    - Combine unexpected concepts

    - Explore unconventional approaches


    Be creative, varied, and thought-provoking.""",

    generate_content_config=types.GenerateContentConfig(

        # Controls randomness: higher values produce more varied and surprising
        # answers. 0.9 is intentionally high so brainstorming is not limited to
        # the safest or most obvious ideas.
        temperature=0.9,

        # Allows up to 2,000 tokens so the agent can develop several ideas with
        # enough detail to make them useful.
        max_output_tokens=2000,

        # Considers tokens until their cumulative probability reaches 0.95. The
        # high value leaves room for less obvious but still plausible wording.
        top_p=0.95,

        # Considers up to 40 likely next tokens. Compared with 10 for the factual
        # agent, this larger pool increases the diversity of generated ideas.
        top_k=40,

        safety_settings=[

            types.SafetySetting(

            # Applies this safety rule to potentially dangerous content.
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,

            # Blocks content rated medium risk or higher. This keeps creative
            # exploration possible while still rejecting more harmful output.
                threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE

                )
        ]
    )

)


# For adk web, we'll use the factual agent as root_agent

# Switch to creative_agent to test different behavior
root_agent = creative_agent