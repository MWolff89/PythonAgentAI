from general_enquries import general_enquiries_engine
from halal_status import population_query_engine
from outlets_address_and_operating_hours import outlets_address_and_operating_hours_engine
from website_and_social_links_vector_query import brands_website_and_social_links_engine


from llama_index.tools import QueryEngineTool, ToolMetadata


tools = [
    # note_engine,
    QueryEngineTool(
        query_engine=outlets_address_and_operating_hours_engine,
        metadata=ToolMetadata(
            name="outlets_address_and_operating_hours_data",
            description="this gives information about outlet address and operating hours. the brand name and/or location is a MUST as an input."
        ),
    ),
    QueryEngineTool(
        query_engine=brands_website_and_social_links_engine,
        metadata=ToolMetadata(
            name="brands_website_and_social_links",
            description="this gives information about the brands website, facebook, instagram and twitter. this is strictly only for brands  links and not for any other links.",
        ),
    ),
    QueryEngineTool(
        query_engine=general_enquiries_engine,
        metadata=ToolMetadata(
            name="general_enquiries",
            description="this gives information about general enquiries."
        )
    ),
     QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="halal_status",
            description="this helps answer questions on which brand(s) are fully halal, not halal or only selected stores within the brand are halal. the input should consist of either a brand name or a choice of [FULLY HALAL, NOT HALAL, SELECTED STORES] OR BOTH. If the user is asking for which brands are halal then we should filter by all that are != NOT HALAL"
        )
    ),

]