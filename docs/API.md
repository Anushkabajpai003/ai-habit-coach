# AI Habit Coach — API Design

_Day 2 Deliverable. No implementation yet — this is the contract Day 3–7 will build against._

All endpoints are server-rendered (Flask + Jinja2), single-user mode, no authentication required for v1.0.

---

### `GET /`
- **Purpose:** Homepage — list all habits with current streaks, check-in controls, and any AI messages/insights.
- **Request:** none
- **Response:** Rendered HTML page
- **Validation:** none
- **Authentication:** none
- **Error cases:** Zero habits → renders empty state cleanly (no error). Database connection failure → renders friendly error page, not a raw traceback.

---

### `POST /habits/new`
- **Purpose:** Create a new habit.
- **Request:** form field `name` (string)
- **Response:** Redirect to `/`
- **Validation:** Reject empty or whitespace-only name (trimmed server-side). Reasonable max length (e.g. 100 chars, matches DB column).
- **Authentication:** none
- **Error cases:** Empty/invalid name → redirect back to `/` with a flash message; no habit created, no crash.

---

### `POST /habits/<id>/delete`
- **Purpose:** Delete a habit and all its associated check-ins.
- **Request:** `id` (path parameter, integer)
- **Response:** Redirect to `/`
- **Validation:** `id` must correspond to an existing habit.
- **Authentication:** none
- **Error cases:** Nonexistent `id` → handled with a graceful 404 or redirect with a flash message, never a raw traceback.

---

### `POST /habits/<id>/checkin`
- **Purpose:** Mark a habit as done for today; creates or updates today's CheckIn record, then returns an AI-generated motivational message.
- **Request:** `id` (path parameter, integer)
- **Response:** Redirect to `/`, homepage re-renders with updated streak and the AI motivational message displayed inline for that habit.
- **Validation:** `id` must exist. Enforce one CheckIn per (habit_id, date) — checking in twice in the same day updates the existing record rather than duplicating (backed by the DB unique constraint from SCHEMA.md).
- **Authentication:** none
- **Error cases:** Claude API failure → check-in still saves successfully; a hardcoded fallback motivational message is shown instead of blocking the action.

---

### `POST /habits/<id>/uncheck`
- **Purpose:** Undo today's check-in (correct a mistaken check-in).
- **Request:** `id` (path parameter, integer)
- **Response:** Redirect to `/`
- **Validation:** `id` must exist; only affects today's CheckIn record, not historical ones.
- **Authentication:** none
- **Error cases:** No check-in exists for today yet → no-op, not an error.

---

### `GET /coach`
- **Purpose:** Render the AI coach chat page with existing session chat history.
- **Request:** none
- **Response:** Rendered HTML chat interface
- **Validation:** none
- **Authentication:** none
- **Error cases:** Empty session history → renders an empty/welcoming chat state, not an error.

---

### `POST /coach/send`
- **Purpose:** Send a user message to the AI coach and receive a contextual reply.
- **Request:** form field `message` (string)
- **Response:** Redirect to `/coach` with updated chat history (both user message and AI reply appended)
- **Validation:** Reject empty messages (ignored, no API call made). Cap message length (e.g. 500 characters) to control API token usage/cost.
- **Authentication:** none
- **Error cases:** Claude API failure → a fallback message like "Your coach is temporarily unavailable, please try again" is shown; the user's message is still preserved in history so it isn't lost.

---

## Summary Table

| Endpoint | Method | Purpose | Auth |
|---|---|---|---|
| `/` | GET | Homepage / habit list | None |
| `/habits/new` | POST | Create habit | None |
| `/habits/<id>/delete` | POST | Delete habit | None |
| `/habits/<id>/checkin` | POST | Check in + get AI motivation | None |
| `/habits/<id>/uncheck` | POST | Undo today's check-in | None |
| `/coach` | GET | Render chat page | None |
| `/coach/send` | POST | Send chat message, get AI reply | None |

This is the complete v1.0 API surface — matches Blueprint Days 3, 4, 5, and 7 exactly, with no endpoints added or removed.
