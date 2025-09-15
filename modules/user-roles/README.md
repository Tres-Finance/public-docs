# TRES User Roles and Capabilities

This guide explains the different user roles available in TRES, their capabilities, and how to manage user access within your organization.

---

## What are User Roles?

User roles in TRES define what actions and data each user can access within your organization. The role-based access control (RBAC) system ensures that users only have access to the features and data they need for their responsibilities.

---

## Available User Roles

TRES supports five distinct user roles, each with different levels of access and capabilities:

### 1. **Admin** - Full Access
**Role ID**: `rol_esWMRtyMWB0Qc6zy`

**Capabilities:**
- **Full System Access**: Complete access to all TRES features and data
- **User Management**: Add, remove, and modify user roles
- **Organization Settings**: Configure all organization-level settings
- **Data Management**: Full access to all transactions, balances, and reports
- **System Administration**: Access to admin-only features and system controls
- **Billing & Subscriptions**: Manage billing and subscription settings
- **API Access**: Full API access with admin permissions
- **Audit Logs**: Access to complete audit trail and system logs

**Use Cases:**
- Organization owners and founders
- Chief Financial Officers (CFOs)
- Senior finance professionals with full control needs
- System administrators
- Senior management with full decision-making authority

**Permissions:**
- `admin:*` - Full administrative access
- `write:*` - Full write access to all data
- `read:*` - Full read access to all data

### 2. **Member** - Standard User
**Role ID**: `rol_jV6pw94d3ihbtIZc`

**Capabilities:**
- **Data Access**: Full access to view all organization data
- **Transaction Management**: Create, edit, and manage transactions
- **Report Generation**: Generate and access all reports
- **Dashboard Access**: Full access to all dashboard features
- **Integration Management**: Configure and manage integrations
- **Cost Basis Operations**: Perform cost basis calculations and adjustments
- **Manual Data Entry**: Add and modify manual transactions
- **Export Functions**: Export data and reports

**Use Cases:**
- Financial analysts
- Accountants
- Portfolio managers
- Operations team members
- Day-to-day users who need full data access

**Permissions:**
- `write:*` - Full write access to all data
- `read:*` - Full read access to all data

### 3. **Viewer** - Read-Only Access
**Role ID**: `rol_O1e1ZnEa26PFm1Eo`

**Capabilities:**
- **Data Viewing**: View all organization data and reports
- **Dashboard Access**: Access to all dashboard widgets and views
- **Report Viewing**: View and download existing reports
- **Export Functions**: Export data for analysis
- **Read-Only Operations**: View transactions, balances, and analytics

**Limitations:**
- **No Data Modification**: Cannot create, edit, or delete transactions
- **No Settings Changes**: Cannot modify organization settings
- **No User Management**: Cannot add or remove users
- **No Integration Changes**: Cannot modify integrations

**Use Cases:**
- External auditors
- Compliance officers
- Board members
- Investors
- Consultants who need data access but not modification rights

**Permissions:**
- `read:*` - Full read access to all data

### 4. **Associate** - Limited Access
**Role ID**: `rol_tvaptlW6AMLeK46H`

**Capabilities:**
- **Limited Data Access**: Access to specific data sets as configured
- **Basic Operations**: Perform basic data entry and viewing tasks
- **Restricted Reports**: Access to pre-approved reports only
- **Limited Dashboard**: Access to specific dashboard widgets

**Limitations:**
- **Restricted Data Access**: Limited to specific accounts or data sets
- **No Administrative Functions**: Cannot access admin features
- **Limited Integration Access**: Restricted integration capabilities
- **Supervised Operations**: May require approval for certain actions

**Use Cases:**
- Junior staff members
- Interns
- External contractors
- Users who need limited, supervised access

**Permissions:**
- Limited permissions based on specific configuration

### 5. **Pending** - Awaiting Approval
**Role ID**: No specific role assigned

**Capabilities:**
- **No Access**: Cannot access any TRES features
- **Awaiting Approval**: User has been invited but not yet approved
- **Email Notifications**: Receives invitation emails and status updates

**Use Cases:**
- New users who have been invited but not yet activated
- Users whose access is temporarily suspended
- Users awaiting role assignment

**Permissions:**
- No permissions until approved and assigned a role

---

## Permission System

### Permission Scopes

TRES uses a hierarchical permission system with the following scopes:

#### **Admin Permissions** (`admin:*`)
- **Full System Control**: Complete administrative access
- **User Management**: Add, remove, and modify users
- **Organization Settings**: Configure all settings
- **System Administration**: Access admin-only features
- **Audit Access**: View complete audit logs

#### **Write Permissions** (`write:*`)
- **Data Modification**: Create, edit, and delete data
- **Transaction Management**: Full transaction operations
- **Report Generation**: Create and modify reports
- **Integration Management**: Configure integrations
- **Manual Operations**: Perform manual data operations

#### **Read Permissions** (`read:*`)
- **Data Viewing**: View all organization data
- **Report Access**: View and download reports
- **Dashboard Access**: Access dashboard features
- **Export Functions**: Export data and reports

### Permission Enforcement

Permissions are enforced at multiple levels:

1. **GraphQL Level**: API endpoints check permissions before execution
2. **UI Level**: Interface elements are hidden based on user permissions
3. **Data Level**: Database queries are filtered based on user access
4. **Feature Level**: Features are enabled/disabled based on user role

---

## User Management

### Adding Users to Your Organization

#### Step 1: Access User Management
1. Log into your TRES dashboard as an Admin
2. Navigate to **Settings** → **User Management**
3. Click **Add User** or **Invite User**

#### Step 2: Invite New Users
1. **Enter Email Addresses**: Add one or more email addresses
2. **Select User Role**: Choose the appropriate role for each user
3. **Send Invitations**: Click **Send Invitations**

#### Step 3: User Acceptance
1. **Email Invitation**: Users receive an email invitation
2. **Account Creation**: New users create their TRES account
3. **Role Assignment**: Users are automatically assigned their role
4. **Access Granted**: Users can now access TRES with their assigned permissions

### Managing Existing Users

#### Changing User Roles
1. Navigate to **Settings** → **User Management**
2. Find the user you want to modify
3. Click **Edit** next to their name
4. Select the new role from the dropdown
5. Click **Save Changes**

#### Removing Users
1. Navigate to **Settings** → **User Management**
2. Find the user you want to remove
3. Click **Remove** next to their name
4. Confirm the removal

#### Suspending User Access
1. Navigate to **Settings** → **User Management**
2. Find the user you want to suspend
3. Click **Suspend** next to their name
4. User access is immediately revoked

---

## Role-Based Feature Access

### Dashboard Access by Role

| Feature | Admin | Member | Viewer | Associate |
|---------|-------|--------|--------|-----------|
| **Overview Dashboard** | ✅ Full | ✅ Full | ✅ Full | ⚠️ Limited |
| **Assets Management** | ✅ Full | ✅ Full | ✅ View Only | ⚠️ Limited |
| **Transactions** | ✅ Full | ✅ Full | ✅ View Only | ⚠️ Limited |
| **Reports** | ✅ Full | ✅ Full | ✅ View Only | ⚠️ Limited |
| **Integrations** | ✅ Full | ✅ Full | ❌ No Access | ⚠️ Limited |
| **User Management** | ✅ Full | ❌ No Access | ❌ No Access | ❌ No Access |
| **Organization Settings** | ✅ Full | ❌ No Access | ❌ No Access | ❌ No Access |
| **Billing & Subscriptions** | ✅ Full | ❌ No Access | ❌ No Access | ❌ No Access |
| **Audit Logs** | ✅ Full | ❌ No Access | ❌ No Access | ❌ No Access |

### API Access by Role

| API Endpoint | Admin | Member | Viewer | Associate |
|--------------|-------|--------|--------|-----------|
| **Read Operations** | ✅ Full | ✅ Full | ✅ Full | ⚠️ Limited |
| **Write Operations** | ✅ Full | ✅ Full | ❌ No Access | ⚠️ Limited |
| **Admin Operations** | ✅ Full | ❌ No Access | ❌ No Access | ❌ No Access |
| **User Management** | ✅ Full | ❌ No Access | ❌ No Access | ❌ No Access |
| **Organization Settings** | ✅ Full | ❌ No Access | ❌ No Access | ❌ No Access |

---

## Best Practices for User Role Management

### 1. **Principle of Least Privilege**
- **Grant Minimum Access**: Only give users the access they need
- **Regular Reviews**: Periodically review user access and permissions
- **Role-Based Assignment**: Assign roles based on job responsibilities
- **Temporary Access**: Use temporary access for specific projects

### 2. **Role Assignment Guidelines**

#### **Admin Role**
- **Finance and Technical Leaders**: Assign to senior finance professionals and technical administrators who need full control
- **Regular Auditing**: Monitor admin actions through audit logs
- **Backup Admins**: Ensure multiple admins for business continuity
- **Documentation**: Document why each user has admin access

#### **Member Role**
- **Standard Users**: Assign to most day-to-day users
- **Training Required**: Ensure users understand their responsibilities
- **Regular Reviews**: Review member access quarterly
- **Clear Boundaries**: Define what members can and cannot do

#### **Viewer Role**
- **External Users**: Ideal for auditors, consultants, and investors
- **Time-Limited Access**: Consider temporary access for external users
- **Data Sensitivity**: Ensure viewers understand data confidentiality
- **Regular Reviews**: Review viewer access regularly

#### **Associate Role**
- **Junior Staff**: Perfect for interns and junior team members
- **Supervised Access**: Ensure proper supervision and training
- **Clear Guidelines**: Provide clear guidelines on what they can access
- **Growth Path**: Plan for role progression as they gain experience

### 3. **Security Considerations**

#### **Access Monitoring**
- **Audit Logs**: Regularly review audit logs for unusual activity
- **Login Monitoring**: Monitor login patterns and locations
- **Permission Changes**: Track all permission and role changes
- **Suspicious Activity**: Set up alerts for suspicious user behavior

#### **Data Protection**
- **Confidentiality**: Ensure users understand data confidentiality requirements
- **Export Controls**: Monitor data exports and downloads
- **Access Logs**: Maintain detailed access logs for compliance
- **Regular Reviews**: Conduct regular access reviews

#### **Compliance Requirements**
- **Regulatory Compliance**: Ensure role assignments meet regulatory requirements
- **Documentation**: Maintain documentation of role assignments and justifications
- **Audit Trail**: Keep complete audit trails for compliance audits
- **Regular Updates**: Update roles and permissions as regulations change

---

## User Role Configuration Examples

### Example 1: Small Organization (5-10 users)

**Recommended Role Distribution:**
- **2 Admins**: CEO/Founder + CFO
- **5-7 Members**: Financial team, operations staff
- **1-2 Viewers**: External accountant, board member

**Configuration:**
```json
{
  "organization": "SmallCorp",
  "users": [
    {
      "email": "ceo@smallcorp.com",
      "role": "admin",
      "justification": "Organization owner"
    },
    {
      "email": "cfo@smallcorp.com", 
      "role": "admin",
      "justification": "Senior finance professional with full control needs"
    },
    {
      "email": "accountant@smallcorp.com",
      "role": "member",
      "justification": "Daily financial operations"
    },
    {
      "email": "external@auditfirm.com",
      "role": "viewer",
      "justification": "External audit access"
    }
  ]
}
```

### Example 2: Medium Organization (20-50 users)

**Recommended Role Distribution:**
- **3-5 Admins**: C-level executives, IT admin
- **15-40 Members**: Financial team, operations, analysts
- **2-5 Viewers**: External auditors, consultants, board members

**Configuration:**
```json
{
  "organization": "MediumCorp",
  "users": [
    {
      "email": "ceo@mediumcorp.com",
      "role": "admin",
      "justification": "Organization owner"
    },
    {
      "email": "cfo@mediumcorp.com",
      "role": "admin", 
      "justification": "Senior finance professional with full control needs"
    },
    {
      "email": "it-admin@mediumcorp.com",
      "role": "admin",
      "justification": "System administration"
    },
    {
      "email": "analyst@mediumcorp.com",
      "role": "member",
      "justification": "Financial analysis"
    },
    {
      "email": "intern@mediumcorp.com",
      "role": "associate",
      "justification": "Limited supervised access"
    }
  ]
}
```

### Example 3: Large Organization (50+ users)

**Recommended Role Distribution:**
- **5-10 Admins**: C-level executives, department heads, IT admin
- **40-80 Members**: Financial team, operations, analysts, managers
- **5-15 Viewers**: External auditors, consultants, board members
- **5-10 Associates**: Junior staff, interns, contractors

**Configuration:**
```json
{
  "organization": "LargeCorp",
  "users": [
    {
      "email": "ceo@largecorp.com",
      "role": "admin",
      "justification": "Organization owner"
    },
    {
      "email": "cfo@largecorp.com",
      "role": "admin",
      "justification": "Senior finance professional with full control needs"
    },
    {
      "email": "it-director@largecorp.com",
      "role": "admin",
      "justification": "IT administration"
    },
    {
      "email": "finance-manager@largecorp.com",
      "role": "member",
      "justification": "Financial management"
    },
    {
      "email": "junior-analyst@largecorp.com",
      "role": "associate",
      "justification": "Supervised analysis work"
    }
  ]
}
```

---

## Troubleshooting User Access Issues

### Common Issues and Solutions

#### **Issue: User Cannot Access TRES**
**Symptoms:**
- User receives "Access Denied" error
- User cannot log in to dashboard
- User sees limited or no data

**Solutions:**
1. **Check User Status**: Verify user is not in "Pending" status
2. **Verify Role Assignment**: Ensure user has been assigned a role
3. **Check Organization Membership**: Confirm user is added to organization
4. **Review Permissions**: Verify user has appropriate permissions
5. **Contact Support**: If issue persists, contact TRES support

#### **Issue: User Has Wrong Permissions**
**Symptoms:**
- User can see data they shouldn't
- User cannot access features they need
- User has more or less access than expected

**Solutions:**
1. **Review Role Assignment**: Check if user has correct role
2. **Update User Role**: Change user role if necessary
3. **Verify Organization Settings**: Check if organization settings affect access
4. **Test Access**: Have user test access after changes
5. **Document Changes**: Keep record of permission changes

#### **Issue: User Cannot Perform Specific Actions**
**Symptoms:**
- User can view data but cannot modify it
- User cannot access certain features
- User receives permission errors

**Solutions:**
1. **Check Role Permissions**: Verify role has required permissions
2. **Review Feature Access**: Check if feature requires specific permissions
3. **Update User Role**: Consider upgrading user role if appropriate
4. **Check Organization Settings**: Verify organization settings allow action
5. **Contact Admin**: Have admin review and adjust permissions

#### **Issue: User Access Changes Not Taking Effect**
**Symptoms:**
- User still has old permissions after role change
- Changes appear to be saved but not applied
- User needs to log out and back in

**Solutions:**
1. **Force Logout**: Have user log out and log back in
2. **Clear Cache**: Clear browser cache and cookies
3. **Wait for Sync**: Allow time for changes to propagate
4. **Verify Changes**: Confirm changes were saved correctly
5. **Contact Support**: If issue persists, contact TRES support

---

## Security and Compliance

### Audit Trail

TRES maintains comprehensive audit logs for all user actions:

#### **User Management Actions**
- User invitations and role assignments
- Permission changes and role modifications
- User additions and removals
- Access suspension and reactivation

#### **Data Access Actions**
- Login and logout events
- Data viewing and export activities
- Transaction modifications and deletions
- Report generation and access

#### **Administrative Actions**
- Organization setting changes
- Integration modifications
- System configuration updates
- Billing and subscription changes

### Compliance Features

#### **Data Protection**
- **Encryption**: All data encrypted in transit and at rest
- **Access Controls**: Role-based access controls
- **Audit Logs**: Complete audit trail for compliance
- **Data Retention**: Configurable data retention policies

#### **Regulatory Compliance**
- **SOX Compliance**: Sarbanes-Oxley compliance features
- **GDPR Compliance**: General Data Protection Regulation compliance
- **SOC 2**: Service Organization Control 2 compliance
- **Custom Compliance**: Configurable compliance frameworks

---

## Related Documentation
- [Organization Settings](./organization-settings/README.md) - How user roles affect organization configuration
- [Security Best Practices](./security/README.md) - Security guidelines for user management
- [API Access Control](./api-access/README.md) - API permissions and access control
- [Audit and Compliance](./audit-compliance/README.md) - Audit trails and compliance features

---

## Summary

User roles and capabilities in TRES provide a comprehensive access control system that ensures:

- **Security**: Users only have access to what they need
- **Compliance**: Meets regulatory and audit requirements
- **Flexibility**: Roles can be customized for different organization needs
- **Scalability**: System grows with your organization
- **Auditability**: Complete audit trail for all user actions

By properly configuring user roles and following best practices, you can ensure that your TRES organization maintains security, compliance, and operational efficiency while providing appropriate access to all team members.
