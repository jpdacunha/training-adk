# DevSecOps Support Agent

> **Deployment notice:** This agent was designed for deployment on **Gemini Enterprise Platform**. It cannot be run locally without adapting its configuration, infrastructure integrations, and credentials.

This multi-agent system, built with the Google Agent Development Kit (ADK), helps analyze and resolve technical incidents.

It first refines the incident report, then cross-references internal knowledge and public sources before proposing a documented resolution.

## Architecture

![Agent workflow diagram](images/image.png)

The coordinator extracts useful incident details and launches the knowledge branches in parallel. The internal branch combines BigQuery and Vertex AI Search; the external branch queries an MCP knowledge base and Google Search.

The results are merged and analyzed by a synthesis agent. Internal sources take priority; external sources are used only when no internal reference exists or when they are explicitly needed as a complement.

## Knowledge Sources

| Branch | Source | Technical access and use | Data storage and known limits |
| --- | --- | --- | --- |
| Internal | BigQuery incident store | `query_bq` calls `find_similar_bugs`, embeds `clean_query` with `text-embedding-004`, then runs BigQuery `VECTOR_SEARCH`. | Relational table set by `BIGQUERY_DATASET` and `BIGQUERY_TABLE` (default: `ops_intelligence.incident_post_mortems`). Reads `title`, `description`, and precomputed `description_embedding`; returns the top three cosine matches. |
| Internal | Vertex AI Search documentation store | `search_vais_agent` invokes `VertexAiSearchTool` with `DATASTORE_ID` and `DATASTORE_LOCATION`, searching with `clean_query`. | Indexed internal documents: matching pages, errors, and procedures. The code does not reveal the data store's source or document types; Vertex AI Search configures them separately. |
| External | Developer knowledge base through MCP | `mcp_kb_agent` obtains callable tools from Agent Registry for the MCP server named by `MCP_SERVER_NAME`. It uses them to retrieve developer documentation, guidelines, runbooks, or incident reports. | MCP exposes tools, not a database schema. The server's backing store, document format, and retrieval implementation are not defined in this repository. |
| External | Public Web through Google Search | `web_search_agent` uses `GoogleSearchTool` to retrieve GitHub issues, Stack Overflow answers, and official documentation. | Google Search indexes public web content. This agent does not own, store, or configure the underlying documents. |

## Deployment Requirements

- Python and the dependencies in `requirements.txt`;
- a configured Google Cloud project;
- a `.env` file defining, among others, `MODEL`, `GOOGLE_CLOUD_PROJECT`, `GOOGLE_CLOUD_LOCATION`, `MCP_SERVER_NAME`, and data-source identifiers;
- Gemini Enterprise Platform resources matching the configured BigQuery, Vertex AI Search, MCP, and Agent Registry integrations.

The agent protects external tool calls by blocking requests containing terms associated with sensitive secrets or credentials.

This example comes from the [Build and Deploy Multi-Agent ADK Systems to Gemini Enterprise lab](https://partner.skills.google/paths/4144/course_templates/1752/labs/633117).

The ADK application exposes the workflow as `support_agent`.