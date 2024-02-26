from general_enquries import general_enquiries_engine
from halal_status import halal_query_engine
from outlets_address_and_operating_hours import outlets_address_and_operating_hours_engine
from website_and_social_links_vector_query import brands_website_and_social_links_engine
# from note_engine import note_engine
from contact_back_engine import contact_back_note_engine
from brand_outlets import brand_outlets_query_engine
from brand_menus import brand_menus_engine
from brand_dine_in import brand_dine_in_query_engine
from llama_index.tools import QueryEngineTool, ToolMetadata


tools = [
    # contact_back_note_engine,
    QueryEngineTool(
        query_engine=outlets_address_and_operating_hours_engine,
        metadata=ToolMetadata(
            name="outlets_address_and_operating_hours_data",
            description="this gives information about outlet address and operating hours. the brand name and/or location is a MUST as an input. The location CANNOT be a region. It must be part of a specific street address or a building name. Do not use this tool if the user's request contains a region such as north, northeast, south, west, east. This tool MUST NOT be used when a user is requesting for ALL outlets of a brand. you should instead use the brand_outlets tool to retrieve all outlets of a brand."
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
        query_engine=brand_menus_engine,
        metadata=ToolMetadata(
            name="brand_menus",
            description="this gives information about brand menus. the input MUST be a brand and/or a food and/or pricing or a food concept such as DINE IN / TAKEAWAY / DELIVERY."
        )
    ),
    QueryEngineTool(
        query_engine=general_enquiries_engine,
        metadata=ToolMetadata(
            name="general_enquiries",
            description="this gives information about general enquiries."
        )
    ),
     QueryEngineTool(
        query_engine=halal_query_engine,
        metadata=ToolMetadata(
            name="halal_status",
            description="this helps answer questions on which brand(s) halal. the input should consist of either a brand name or a choice of [FULLY HALAL, NOT HALAL, SELECTED STORES] OR BOTH. If the user has not provided a brand but instead is asking in general for which brands are halal then we should filter by all that are != NOT HALAL OR filter by FULLY HALAL OR SELECTED STORES. If the user has provided a brand then we should filter by that brand and return the halal status of that brand."
        )
    ),
    QueryEngineTool(
        query_engine=brand_outlets_query_engine,
        metadata=ToolMetadata(
            name="brand_outlets",
            description="this helps answer questions on brand outlets. the input should consist of either a brand name or part of an address. This tool should be used if the user is asking for nearest outlets to a region, in which case simply return all outlets from the brand. this tool should also be used when a user is requesting for ALL outlets of a brand."
        )
    ),
    QueryEngineTool(
            query_engine=brand_dine_in_query_engine,
            metadata=ToolMetadata(
                name="brand_dine_in",
                description="this helps answer questions on the brand outlets which offer dine in. the input should consist of optionally a brand name. This tool should be used if the user is asking for which brands or outlets of a brand offer dine in. this tool should also be used when a user is requesting for ALL brands that offer dine in. If the user is asking for which brands offer dine in then return all results before using the results to infer the brands which offer dine in."
            )
        ),
]