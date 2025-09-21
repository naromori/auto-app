# Project Refactoring Plan

## 🏗️ **Architecture & Structure Improvements**

### 1. **Dependency Injection & Singleton Issues**
- **Replace singleton logger pattern** with proper dependency injection
- **Extract app-wide services** (database, logger, config) into a service container
- **Remove direct imports of singletons** from modules to improve testability

### 2. **Import & Module Organization**
- **Consolidate relative imports** - use absolute imports from `src` root consistently
- **Create proper `__init__.py` exports** for cleaner import statements
- **Remove unused imports** and organize import order (stdlib → third-party → local)

### 3. **Database Architecture**
- **Move models to separate module** (`src/models/`) instead of in connection.py
- **Add proper database migrations** system for schema changes
- **Implement repository pattern** consistently for all data access
- **Add connection pooling** and proper error handling

## 🛡️ **Error Handling & Validation**

### 4. **Exception Handling**
- **Create custom exception classes** for different error types (ValidationError, DatabaseError, etc.)
- **Add comprehensive error handling** in database operations
- **Implement proper error boundaries** in UI components

### 5. **Input Validation**
- **Centralize validation logic** - move from inline validation to dedicated validators
- **Add server-side validation** for all user inputs
- **Implement sanitization** for database inputs

## 🎨 **UI & UX Improvements**

### 6. **Screen Management**
- **Extract common screen functionality** into base classes
- **Implement proper navigation history** and back button handling
- **Add loading states** and user feedback for async operations

### 7. **Component Reusability**
- **Create reusable UI components** (error dialogs, form fields, etc.)
- **Standardize common patterns** (form validation, error display)

## 🔧 **Code Quality & Maintenance**

### 8. **Configuration Management**
- **Add environment-specific settings** (database paths, logging levels)
- **Implement proper secrets management** for sensitive configuration
- **Add configuration validation** on startup

### 9. **Logging & Monitoring**
- **Implement structured logging** with consistent format
- **Add performance monitoring** for database queries and UI operations
- **Create log rotation** and proper cleanup

### 10. **Testing Infrastructure**
- **Add unit tests** for business logic (validators, repositories)
- **Implement integration tests** for database operations
- **Add UI automation tests** for critical user flows

## 📁 **File Structure Reorganization**

### 11. **New Directory Structure**
```
src/
├── models/          # Database models
├── repositories/    # Data access layer
├── services/       # Business logic services
├── ui/
│   ├── components/ # Reusable UI components
│   ├── screens/    # Screen implementations
│   └── themes/     # Theme definitions
├── core/           # App initialization, DI container
├── utils/          # Pure utility functions
└── config/         # Configuration management
```

## 🚀 **Implementation Priority**

**Phase 1 (High Priority):**
- [ ] Fix import organization and module structure
- [ ] Implement proper error handling
- [ ] Extract database models from connection.py
- [ ] Add input validation and sanitization

**Phase 2 (Medium Priority):**
- [ ] Refactor singleton pattern to dependency injection
- [ ] Implement reusable UI components
- [ ] Add comprehensive logging
- [ ] Create configuration validation

**Phase 3 (Future Enhancements):**
- [ ] Add testing infrastructure
- [ ] Implement performance monitoring
- [ ] Add database migrations
- [ ] Enhance navigation and user experience

## 🔍 **Specific Issues Found**

### Current Issues to Address:

1. **src/main.py:51** - TODO comment about config implementation
2. **src/main.py:56** - Temporary theme configuration needs proper management
3. **Database closing in user_repository.py:22** - Should not close DB connection in repository
4. **Hardcoded file paths** - KV file paths should be configurable
5. **Inline imports** - Several modules have imports inside functions (e.g., auth_login.py:91)
6. **Inconsistent logging** - Some modules use different logging patterns
7. **No error handling** - Missing try-catch blocks for database operations
8. **Password validation logic** - Area code validation is too restrictive (data_validator.py:35)

## 📋 **Detailed Action Items**

### Immediate Actions (Phase 1):
1. Create `src/models/user.py` and move UserModel from connection.py
2. Fix database connection management in repositories
3. Create custom exception classes in `src/exceptions/`
4. Standardize import statements across all modules
5. Add proper error handling to all database operations
6. Create base screen class with common functionality
7. Extract snackbar logic into reusable component

### Medium-term Actions (Phase 2):
1. Implement dependency injection container
2. Create service layer for business logic
3. Add configuration validation on app startup
4. Implement proper logging rotation
5. Create reusable form validation components
6. Add loading states to all async operations

### Long-term Actions (Phase 3):
1. Set up testing framework (pytest + pytest-kivy)
2. Add database migration system
3. Implement proper navigation stack
4. Add performance monitoring
5. Create automated UI tests
6. Add internationalization support