# -*- coding: utf-8 -*-
""" Data models for LangGraph workflow with agents (includes state model)
data_models.py
"""

from typing import Dict, List, Any, Optional, TypedDict


class ApplicationData(TypedDict):
    concept_name: str  # Name of the concept this application relates to
    name: str
    brief_description: str
    images: List[Dict[str, Any]]  # List of image data, including URL
    description: str  # Detailed description of the application
    RoadmapData: Optional[
        List["RoadmapData"]
    ]  # Optional roadmap data for learning this application


class RoadmapData(TypedDict):
    application: str
    title: str
    description_1: []
    description_2: []
    description_3: [] 
    # description is a list of tuples, each tuple contains a description, estimated_time, and prerequisites, we would excpect the most prominent concepts to be listed. 



class WorkflowState(TypedDict):
    """State structure for the LangGraph workflow"""
    uuid: str  # Unique identifier for the workflow instance
    document_path: str
    text_input: str
    user_metadata: Dict[str, Any]  # interests, career goals, education_level, backgroundn, hobbies.
    relevant_concepts: List[Dict[str, Any]]  # Major theorems/phenomena only
    concept_applications: Dict[
        str, List[ApplicationData]
    ]  # Key: concept name, Value: list of applications
    last_applications_timestamp = Optional[str]
    last_roadmap_timestamp = Optional[str]
    error: Optional[str]
