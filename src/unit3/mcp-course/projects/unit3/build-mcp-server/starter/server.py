#!/usr/bin/env python3
"""
Module 1: Basic MCP Server - Starter Code
TODO: Implement tools for analyzing git changes and suggesting PR templates
"""

import json
import subprocess
from pathlib import Path
from typing import Optional
from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("pr-agent")

# PR template directory (shared across all modules)
TEMPLATES_DIR = Path(__file__).parent.parent.parent / "templates"

# Default PR templates
DEFAULT_TEMPLATES = {
    "bug.md": "Bug Fix",
    "docs.md": "Documentation",
    "feature.md": "Feature",
    "performance.md": "Performance",
    "refactor.md": "Refactor",
    "security.md": "Security",
    "test.md": "Test"
}

# Type mapping for PR templates
TYPE_MAPPING = {
    "bug": "bug.md",
    "fix": "bug.md",
    "feature": "feature.md",
    "enhancement": "feature.md",
    "docs": "docs.md",
    "documentation": "docs.md",
    "refactor": "refactor.md",
    "cleanup": "refactor.md",
    "test": "test.md",
    "testing": "test.md",
    "performance": "performance.md",
    "optimization": "performance.md",
    "security": "security.md"
}

@mcp.tool()
async def analyze_file_changes(base_branch: str = "main",
                                include_diff: bool = True,
                                max_diff_lines : int = 500,
                                working_directory: Optional[str] = None) -> str:
    """Get the full diff and list of changed files in the current git repository.
    
    Args:
        base_branch: Base branch to compare against (default: main)
        include_diff: Include the full diff content (default: true)
        max_diff_lines: Maximum number of lines to include in the diff (default: 500)
        working_directory: Directory to run git commands in (default: current directory)
    """


    # Get the working directory
    try:
        if working_directory is None:
            context = mcp.get_context()
            roots_result = await context.session.list_roots()
            working_directory = roots_result.roots[0].uri.path
    except Exception as e:
        print(f"Error getting working directory: {e}")
        pass

    # Get the diff
    try:
        result = subprocess.run(["git", "diff", f"{base_branch}...HEAD"],
                                capture_output=True,
                                text=True,
                                cwd=working_directory)
        
        diff_output = result.stdout
        diff_lines = diff_output.split('\n')

        # smart truncation if needed
        if len(diff_lines) > max_diff_lines:
            truncated_diff = "\n".join(diff_lines[:max_diff_lines])
            truncated_diff += "\n\n... Output truncated. Showing {max_diff_lines} lines of {len(diff_lines)} lines ...."
            diff_output = truncated_diff
        
        # Get summary statistics
        stats_result = subprocess.run(
            ["git", "diff", "--stat", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True
        )

        # Get changed files
        files_result = subprocess.run(
            ["git", "diff", "--name-status", f"{base_branch}...HEAD"],
            capture_output=True,
            text=True,
            cwd=working_directory
        )

        return json.dumps({
            "stats": stats_result.stdout,
            "total_lines": len(diff_lines),
            "diff": diff_output if include_diff else "Use include_diff=true to see diff",
            "files_changed": files_result.stdout.splitlines()
        })
    
    except Exception as e:
        return json.dumps({"error": str(e)})


@mcp.tool()
async def get_pr_templates() -> str:
    """List available PR templates with their content."""
    templates = [
        {
            "filename": filename,
            "type": template_type,
            "content": (TEMPLATES_DIR / filename).read_text()
        }
        for filename, template_type in DEFAULT_TEMPLATES.items()
    ]

    return json.dumps(templates, indent=2)


@mcp.tool()
async def suggest_template(changes_summary: str, change_type: str) -> str:
    """Let Claude analyze the changes and suggest the most appropriate PR template.
    
    Args:
        changes_summary: Your analysis of what the changes do
        change_type: The type of change you've identified (bug, feature, docs, refactor, test, etc.)
    """

    templates_response = await get_pr_templates()
    templates_response = json.loads(templates_response)

    # Find matching template
    template_file = TYPE_MAPPING.get(change_type.lower(), "feature.md")
    selected_template = next(
        (t for t in templates_response if t["filename"] == template_file),
        templates_response[0] # Default to first template if no match
    )

    suggestion = {
        "recommended_template": selected_template,
        "reasoning": f"Based on your analysis: '{changes_summary}', this appears to be a {change_type} change.",
        "template_content": selected_template["content"],
        "usage_hint": "Claude can help you fill out this template based on the specific changes in your PR."
    }

    return json.dumps(suggestion, indent=2)


if __name__ == "__main__":
    mcp.run()