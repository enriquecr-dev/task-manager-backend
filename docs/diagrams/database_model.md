# Database Entity-Relationship Model

```mermaid
erDiagram
    USERS {
        uuid id PK
        string email
        string hashed_password
        boolean is_active "Soft delete flag"
        datetime created_at
    }
    PROJECTS {
        uuid id PK
        string name
        string description
        boolean is_active
        uuid owner_id FK
    }
    PROJECT_MEMBERS {
        uuid user_id FK
        uuid project_id FK
        string role "Admin, Member, Viewer"
    }
    TASKS {
        uuid id PK
        string title
        string description
        string status "To Do, In Progress, Review, Done"
        string priority
        uuid project_id FK
        uuid assignee_id FK
    }

    USERS ||--o{ PROJECTS : "owns"
    USERS ||--o{ PROJECT_MEMBERS : "belongs to"
    PROJECTS ||--o{ PROJECT_MEMBERS : "has members"
    PROJECTS ||--o{ TASKS : "contains"
    USERS ||--o{ TASKS : "assigned to"
    