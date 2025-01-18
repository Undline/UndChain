
# **Documentation Structure for M3L and GSS**

#### **1. Introduction**

- Overview of M3L and GSS.
- Purpose: Simplify UI/UX development with modularity and cross-application consistency.
- Key Features:
    - M3L defines page **structure** and **intents**.
    - GSS defines **styling**, **interactions**, and **accessibility**.

#### **2. Core Concepts**

- **M3L Basics**:
    - Meta Information (`title`, `description`, `author`).
    - `rating` table: `classification`, `public_approval`, `mimic_content_ID`.
    - Structure of the page (`layout`, `containers`, `content`).
- **GSS Basics**:
    - Global styles and themes.
    - Widget-specific styling.
    - Accessibility standards (e.g., tooltips, focus states).

#### **3. Intents and Events**

- **Intents in M3L**:
    - High-level actions (e.g., `accept`, `help`, `browse`).
    - How intents define **what** should happen.
- **Events in GSS**:
    - Mapping intents to user interactions (e.g., `on click`, `on hover`).
    - Input modality adaptability (mouse, touch, controller).

#### **4. Co-Chain Integration**

- How M3L connects with co-chains (e.g., SQeeL, Mimic).
- Resource links and dynamic updates.
- Examples:
    - Using SQeeL for asset grids.
    - Using Mimic for contextual guidance.

#### **5. Widgets**

- **Standard Widgets**:
    - `asset_grid`, `carousel`, `nav_menu`, `tooltip`, etc.
    - Required and optional fields.
- **Custom Widgets**:
    - How developers can define and integrate custom widgets.
- **State Management**:
    - Defining widget states (`active`, `disabled`, etc.) in M3L.

#### **6. Accessibility**

- Best practices for creating accessible GSS files.
- Examples:
    - Tooltips and focus management.
    - Color contrast recommendations.

#### **7. Examples**

- Full examples of M3L and GSS files:
    - Marketplace with carousel and asset grid.
    - Simple static content page with a hero section.
- Step-by-step walkthrough of building a page.

#### **8. Event Handling**

- How errors are managed via GSS (e.g., error widgets).
- How to style other types of events such as information, warning, confirmation (for purchases) and notification (for messages)
- How these various event types can be triggered
- Best practices for fallback behavior.

#### **9. Future Proofing**

- Placeholder fields for co-chains (e.g., `mimic_content_ID`).
- Suggestions for extending M3L and GSS (e.g., VR support, BMI (brain machine interface).

---

# Introduction to M3L and GSS

## Overview

M3L (Multi-Media Markup Language) and GSS (Global Style Sheets) are modular frameworks designed to simplify UI/UX development for decentralized applications (dApps), offering a seamless way to integrate structure and styling while ensuring compatibility with decentralized ecosystems. By separating structure and styling, M3L and GSS allow developers and designers to collaborate seamlessly while maintaining flexibility and performance.

### Purpose

- **M3L**: Defines the logical structure and functionality of the application. It focuses on the "what" by describing the page layout, widget configurations, and user intents.
- **GSS**: Manages the visual design and user interactions. It focuses on the "how" by defining styling, animations, and event mappings for different input modalities (mouse, touch, controller).

Together, M3L and GSS create a consistent and adaptable UI/UX environment across applications and devices.

### Key Features

#### **1. Separation of Structure and Styling**

M3L handles page layout and functionality, while GSS ensures consistent theming and interaction design. This separation allows:

- Developers to focus on application logic.
- Designers to focus on creating visually appealing and accessible designs.

#### **2. Modularity and Reusability**

- **M3L** defines high-level widgets like `asset_grid`, `carousel`, and `nav_menu` that can be reused across applications.
- **GSS** provides global styling rules, ensuring a consistent look and feel across all dApps using the same theme.

#### **3. Adaptability for Input Types**

GSS supports multiple input types (mouse, touch, controller) and allows developers to define how interactions are handled for each.

#### **4. Co-Chain Integration**

M3L seamlessly integrates with co-chains like SQeeL and Mimic:

- **SQeeL** handles data queries for widgets like `asset_grid`.
- **Mimic** provides contextual guidance and assistance.

#### **5. Performance Optimization**

- Once loaded, GSS files remain consistent across applications, reducing network traffic and computation.
- Shared styles enhance cross-application performance.

### Widget Overview

M3L and GSS support a diverse range of widgets, categorized into **Low-Level Widgets** and **High-Level Widgets**:

#### **Low-Level Widgets**

- **Button**: Image buttons, confirmation buttons, call-to-action buttons, and muted buttons.
- **Text**: H1-H5 headers, ordered and unordered lists, highlighter text, hyperlinks and paragraph text.
- **Text Box**: Allows for single-line user input.
- **Text Area**: Multi-line input for larger text blocks.
- **Checkbox**: For binary selections.
- **Radio Button**: Allows a single selection from multiple options.
- **Navigation Box (Text Bar)**: A widget designed for displaying and interacting with breadcrumbs, helping users navigate hierarchical structures such as file systems, page directories, or web navigation paths.
- **Scroll Area**: Indicates additional content is available via scroll or pan.
- **Drop Menu**: A dropdown list of options.
- **Sliders**: For selecting a value or range within a spectrum.
- **Tooltip**: Provides contextual information when a user hovers or focuses on an element.
- **Progress Bar**: Visualizes progress toward a goal.
- **Cards**: Compact content containers often used for showcasing assets or information.
- **Posters**: Larger cards that dominate the view, particularly on mobile.
- **Window**: Defines the background and foreground containers for widgets (like a frame).
- **Canvas**: A flexible draw area for custom shapes or graphics.
- **Carousel**: Automatically cycles through various content, like images or promotions.
- **Toolbar**: Houses multiple buttons or tools for modifying a target section.
- **Floating Menu**: Context-sensitive menu that activates on events (e.g., right-click, hover).
- **Graph (Interactive)**: Generates visualizations based on input data; allows interactions if the data is editable.
- **Timeline**: A graph-like structure for events over time, expanding only horizontally.
- **Spellcheck**: Highlights misspelled words with corrections shown in a tooltip.
- **Item Grid**: Displays items in a controller-friendly layout.
- **Tab Widget**: Groups widgets by category, activated via tabs.
- **Video**: Plays videos with predefined controls and settings.
- **Popup**: Creates modals for warnings, errors, confirmations, or informational messages.
- **Date Picker**: Allows users to select dates.
- **Tree View**: Represents hierarchical data (e.g., directories).
- **Poll Widget**: Presents a multiple-choice question and shows aggregated results.
- **Status Bar**: Displays relevant statistics or information at the bottom of the screen.
- **Split View**: Divides the screen into two or more resizable panels.
- **Breadcrumbs**: Shows the user’s current location in a hierarchy, improving navigation and enhancing both SEO and accessibility by providing semantic structure and clear navigational aids.

#### **High-Level Widgets**

- **Asset View**: Provides a comprehensive shopping experience with product grids, sorting tools, a shopping cart, and detailed asset sections.
- **Node View**: Enables flowcharting, visual programming, or editing workflows.
- **Spreadsheet**: A grid-like table supporting formulas, edits, and data visualization.
- **Text Editor**: Rich text editing with formatting tools, suggestions, and AI-powered generation.
- **IDE**: A code editor with syntax highlighting, debugging tools, and project navigation.
- **Content Area**: Combines a canvas, sidebars, and list views for CAD or visual editing tasks.
- **Map**: Displays geographic or abstract data with layers, POIs, and animations.
- **Toast**: Temporary notifications with a history button and silencer mode.
- **Chat Widget**: Supports real-time messaging, reactions, and user status indicators.
- **Forum Widget**: Enables threaded discussions for asynchronous communication.
- **Video Player**: Advanced media playback with interactivity, previews, and OSTR (On-Screen Text Reader).
- **Live View**: Allows interactive presentations or remote tutorials.
- **Hero Section**: Captures user attention with headers, subheaders, and call-to-action buttons.
- **Wiki View**: Editable content area with permissions and collaboration tools.
- **News Feed**: Displays content in a scrollable feed with filters.
- **Wizard Widget**: Guides users through multi-step processes or settings.
- **Dashboard**: Aggregates widgets like graphs and spreadsheets for data visualization and navigation.

### Why Use M3L and GSS?

1. **Simplicity**:
    
    - Clean, readable syntax makes it easy to define application structure and styling.
    - Developers no longer need to mix logic and presentation.
2. **Consistency**:
    
    - GSS themes provide a unified look and feel, ensuring user familiarity across different applications.
3. **Extensibility**:
    
    - M3L and GSS are designed to support future features like VR, voice input, and AI-driven interfaces. For example, Mimic could analyze user behavior and provide contextual guidance or suggestions, such as highlighting the best path through a shopping application based on previous preferences, or enabling advanced voice commands for navigation and data entry.
4. **Developer and Designer Collaboration**:
    
    - M3L defines what happens, while GSS defines how it happens, creating a clear boundary between development and design.

### Example Workflow

1. **Developer** creates an M3L file defining the structure and functionality of the page.
2. **Designer** writes a GSS file that applies global styling and interaction rules.
3. **Co-Chain Integration**:
    - The M3L file references resource links from co-chains like SQeeL or Mimic.
    - Co-chains provide dynamic content or contextual assistance as needed.

### Who Should Use This Documentation?

This documentation is intended for developers building applications with M3L and GSS. It provides:

- A technical understanding of how to define page structures and intents in M3L.
- Guidelines for creating consistent and accessible styling in GSS.
- Examples and best practices for integrating co-chains and handling dynamic content.

By the end of this documentation, you will have a clear understanding of how to build modular, scalable, and visually consistent applications using M3L and GSS.

---

# Core Concepts

## M3L Basics

M3L focuses on defining the logical structure and functionality of your application. It provides a clean, declarative syntax for laying out pages, configuring widgets, and specifying user intents.

### Key Components

#### **1. Meta Information**

Meta information is used to describe the overall purpose and categorization of the page. Common fields include:

```toml
[meta]
title = "Page Title"
description = "Brief description of the page."
author = "@username"

[rating]
classification = "Everyone"  # Content rating for audience suitability.
public_approval = 85          # Sentiment score based on user feedback ranges between 0 - 100. 0 means no rating.
mimic_content_ID = ""        # Placeholder for Mimic integration.
content_type = "marketplace" # Defines the type of page.
```

#### **2. Layout and Containers**

The `layout` section defines the structure of your page using containers. Containers are flexible, allowing you to group and organize content hierarchically.

```toml
[layout]
[[layout.container]]
id = "main"
type = "grid"
intention = "browse"
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" },
    # { link = "@Auction_House/asset_list.csv", type = "grid_items" } # Uncomment for debugging with static data
]

[[layout.container]]
id = "footer"
type = "static_content"
source = "@Auction_House/promotions.md"
```

### Intents

Intents describe **what** an element is meant to do. They are high-level actions like `browse`, `accept`, or `navigate`. Intents are defined in the M3L file and mapped to specific events in the GSS file.

```toml
[[layout.container.content]]
type = "buy_button"
intention = "accept"
resources = [
    { link = "SQeeL://Auction_House/buy" },
    { link = "Mimic://User_Guide/buy_button" }
]
```

### Resources

Resources define the data or actions associated with a widget. These can come from co-chains like SQeeL or Mimic, or from pre-defined text sources such as a CSV file. For example, static resources can be used during development for debugging purposes or to create applications with fixed content.

```toml
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" },
    { link = "Mimic://Recommendations/asset_grid", type = "recommendations" }
]
```

## GSS Basics

GSS defines how elements in the M3L file are styled and how users interact with them. It supports global theming, event mappings, and accessibility features.

### Key Components

#### **1. Global Styling**

GSS files provide a consistent look and feel across applications by defining global styles for fonts, colors, and layouts.

```toml
[global]
body.font-family = "Orbitron, sans-serif"
body.background-color = "#f0f0f0"
body.color = "#333"
```

#### **2. Widget-Specific Styling**

Each widget type in M3L can have specific styles defined in GSS.

```toml
[buy_button]
background-color = "#007BFF"
color = "#fff"
padding = "10px"
border-radius = "5px"
hover.background-color = "#0056b3"
```

#### **3. Event Mapping**

Events map M3L intents to specific interactions based on input types (mouse, touch, controller). Generic button names such as `Action`, `Cancel`, and `Menu` allow developers to create device-independent mappings. This ensures that controllers can be dynamically remapped based on user preferences or device capabilities.

```toml
[buy_button.interactions]
accept.mouse = "on click"
accept.touch = "on long press"
accept.controller = "on button press:Action"
```

#### **4. Animations**

GSS can define animations for dynamic content and transitions.

```toml
[animations.fade_in]
type = "fade-in"
duration = "1s"
trigger = "on load"
target = "carousel.item"
```

#### **5. Accessibility Features**

Accessibility options ensure that all users can interact effectively with the application. For example, M3L widgets support keyboard navigation using `tab` and `enter`, while GSS can define properties like `aria-label` for screen readers. Accessibility options like tooltips and focus management can be defined in GSS.

```toml
[tooltip]
background-color = "#000"
color = "#fff"
font-size = "12px"
padding = "5px"
trigger.help.mouse = "on hover"
trigger.help.touch = "on tap"
```

### Summary

M3L and GSS work together to define the structure and styling of your application. M3L provides the logical foundation, while GSS ensures a consistent, accessible, and engaging user experience across all applications.

---

# Intents and Events

## Intents in M3L

Intents in M3L describe **what** a widget or element is meant to do. They are high-level actions that specify the purpose of a widget without prescribing how the interaction occurs. This abstraction allows developers to define functionality in a declarative manner, leaving the specifics of user interaction to GSS.

### Examples of Intents

- **`navigate`**: Directs the user to another page or section of the application, such as hyperlinks or buttons that jump to a different screen.
- **`accept`**: Represents a primary action, such as confirming a purchase or submitting a form.
- **`help`**: Indicates a need for contextual assistance, such as displaying a tooltip or triggering guidance from Mimic.
- **`browse`**: Used for navigational or exploratory actions, such as scrolling through a grid of assets.
- **`cancel`**: Represents actions to close or abort a process.
- **`toggle`**: Switches the state of a widget, such as turning a feature on or off.

Note: Intents also support Markdown as the standard format for text, allowing inline navigation links and resource integration. This ensures developers have a familiar and flexible way to manage text-based linking.
### Defining Intents in M3L

Intents can handle navigation by specifying links to other M3L pages or resources. This is common for buttons, hyperlinks, or navigation menus. Intents are specified within the `layout.container.content` section in an M3L file. Each intent is associated with a widget type and optional resources to define its behavior.

#### Examples:

**Primary Action (Accept Intent):**

```toml
[[layout.container.content]]
type = "buy_button"
intention = "accept"
resources = [
    { link = "SQeeL://Auction_House/buy" },
    { link = "Mimic://User_Guide/buy_button" }
]
```

In this example:

- The widget type is `buy_button`.
- The intent is `accept`, indicating a primary action.
- Resources link to co-chains that handle the associated functionality.

**Navigation (Navigate Intent):**

```toml
[[layout.container.content]]
type = "hyperlink"
intention = "navigate"
resources = [
    { link = "@Undline/my_assets.m3l" } # Points to another M3L page on the creator's site
]
text = "View all my assets"
```

In this example:

- The widget type is `hyperlink`.
- The intent is `navigate`, specifying that clicking the link will navigate to another page.
- The resource defines the destination of the link.

**In-Line Markdown Links:**

```markdown
For more details, [click here](@Undline/my_assets.m3l).
```

- Inline navigation links can use Markdown syntax to reference M3L pages or co-chain resources.

**Images with Markdown:**

```markdown
![Product Image](@Undline/assets/image.jpg)
```

- Images can reference local assets or external resources using similar Markdown conventions.
- The resource defines the destination of the link.

**Contextual Help (Help Intent):**

```toml
[[layout.container.content]]
type = "tooltip"
intention = "help"
description = "Hover here for more information."
resources = [
    { link = "Mimic://Help/tooltip_assistance" }
]
```

In this example:

- The widget type is `tooltip`.
- The intent is `help`, requesting contextual assistance.
- Resources link to co-chains like Mimic for guidance.

**Exploration (Browse Intent):**

```toml
[[layout.container.content]]
type = "asset_grid"
intention = "browse"
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" }
]
```

In this example:

- The widget type is `asset_grid`.
- The intent is `browse`, enabling users to explore the grid of assets.
- Resources provide the data for the grid items.

**Cancel Action (Cancel Intent):**

```toml
[[layout.container.content]]
type = "cancel_button"
intention = "cancel"
resources = [
    { link = "SQeeL://Auction_House/cancel_order" }
]
```

In this example:

- The widget type is `cancel_button`.
- The intent is `cancel`, allowing users to abort a process.
- Resources define the action for cancellation.

**State Toggle (Toggle Intent):**

```toml
[[layout.container.content]]
type = "switch"
intention = "toggle"
resources = [
    { link = "SQeeL://Settings/toggle_feature" }
]
```

In this example:

- The widget type is `switch`.
- The intent is `toggle`, enabling users to change a state.
- Resources handle the logic for the toggle action.

## Events in GSS

Events in GSS define **how** user interactions map to intents specified in M3L. This separation ensures flexibility, as developers can adapt interactions for different devices and input modalities.

### Event Mapping

Event mapping connects M3L intents to specific user interactions. GSS supports multiple input types, such as:

- **Mouse**: `on click`, `on hover`
- **Touch**: `on tap`, `on long press`
- **Controller**: `on button press:Action`

#### Example:

```toml
[buy_button.interactions]
accept.mouse = "on click"
accept.touch = "on long press"
accept.controller = "on button press:Action"
```

### Input Modality Adaptability

GSS enables developers to define device-independent interactions using generic input mappings, such as:

- **`Action`**: The primary button for confirmation or selection.
- **`Cancel`**: The secondary button for closing or dismissing.
- **`Menu`**: For accessing additional options.

This system allows for seamless remapping of controls and ensures consistent behavior across devices.

### Advanced Example with Multiple Intents

```toml
[tooltip.interactions]
help.mouse = "on hover"
help.touch = "on tap"
help.controller = "on button press:Menu"

[buy_button.interactions]
accept.mouse = "on click"
accept.touch = "on long press"
accept.controller = "on button press:Action"

[cancel_button.interactions]
cancel.mouse = "on click"
cancel.touch = "on double tap"
cancel.controller = "on button press:Cancel"
```

In this example:

- The `tooltip` widget responds to the `help` intent based on input type.
- The `buy_button` widget maps the `accept` intent to different interactions depending on the device.
- The `cancel_button` maps the `cancel` intent to device-specific interactions.

### Summary

- **M3L Intents**: Define high-level actions that describe **what** should happen.
- **GSS Events**: Map intents to specific interactions, defining **how** users perform those actions.

This separation of concerns enhances modularity, adaptability, and maintainability, making M3L and GSS ideal for modern, multi-device applications.

---

# Co-Chain Integration

## Overview

M3L and GSS seamlessly integrate with co-chains to provide dynamic content, contextual guidance, and enhanced functionality. By leveraging co-chain resource links, developers can create applications that pull data, interact with AI systems, and maintain real-time updates—all within a decentralized ecosystem.

### Key Co-Chains

1. **Pages**: The co-chain where M3L and GSS are created and managed. It acts as the backbone for content delivery and UI/UX definitions.
2. **SQeeL**: Handles data queries, enabling applications to fetch and display structured data in widgets like `asset_grid` or `spreadsheet`.
3. **Mimic**: Reads contextual information, such as tooltips, to provide AI-powered guidance and suggestions.
4. **Live**: Supports live streaming and interactive content, such as video tutorials or collaborative sessions.
5. **Code Ledger**: Acts as a decentralized repository framework for managing and editing codebases.

## Resource Links

Resource links in M3L are the foundation for co-chain integration. These links point to specific co-chain resources, enabling dynamic data retrieval or actions. The order in which co-chains are listed determines their priority. For example, if two co-chains attempt to act on the same widget, the first-listed co-chain has precedence.

### Example Resource Link:

```toml
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" },
    { link = "Mimic://Recommendations/asset_grid", type = "recommendations" }
]
```

- **`SQeeL://Auction_House/assets.db`**: Fetches asset data for the `asset_grid` widget.
- **`Mimic://Recommendations/asset_grid`**: Provides recommendations for displayed assets.

## Dynamic Updates

Dynamic updates allow widgets to refresh their content automatically based on changes in co-chain data or user actions. This ensures that applications remain responsive and up-to-date.

### Example: Dynamic Asset Grid

```toml
[[layout.container.content]]
type = "asset_grid"
intention = "browse"
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" }
]
update_on = "filter_change"
```

- **`update_on`**: Triggers the grid to refresh when a filter is applied or modified.

## Examples of Co-Chain Integration

### **1. Using SQeeL for Asset Grids**

```toml
[[layout.container.content]]
type = "asset_grid"
intention = "browse"
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" }
]
```

- **Description**: The `asset_grid` widget fetches and displays data from the SQeeL co-chain. It supports sorting, filtering, and pagination based on the provided dataset.

### **2. Using Mimic for Contextual Guidance**

```toml
[[layout.container.content]]
type = "tooltip"
intention = "help"
description = "Hover here for more information."
resources = [
    { link = "Mimic://Help/tooltip_assistance" }
]
```

- **Description**: While the developer defines the tooltip content, Mimic can read this information to provide enhanced contextual guidance or suggestions to users.

### **3. Using Live for Video Streaming**

```toml
[[layout.container.content]]
type = "video_player"
intention = "browse"
resources = [
    { link = "Live://Tutorials/getting_started" }
]
```

- **Description**: The `video_player` widget integrates with the Live co-chain to deliver live or recorded video content, enabling tutorials, collaborative sessions, or presentations.

### **4. Using Code Ledger for Code Management**

```toml
[[layout.container.content]]
type = "ide"
intention = "edit"
resources = [
    { link = "CodeLedger://Projects/MyProject" }
]
```

- **Description**: The `ide` widget connects to the Code Ledger co-chain, allowing developers to manage, edit, and collaborate on codebases in a decentralized environment.

## Summary

- **Pages**: Hosts M3L and GSS, providing a decentralized environment for creating and managing content.
- **SQeeL**: Powers data-driven widgets with robust querying capabilities.
- **Mimic**: Reads contextual information like tooltips to enhance user interactions with AI-driven assistance.
- **Live**: Facilitates live streaming and video content for tutorials and collaborations.
- **Code Ledger**: Serves as a decentralized repository for managing and editing codebases.

By integrating co-chains, M3L and GSS enable applications to deliver dynamic, responsive, and intelligent experiences tailored to user needs.

---

# Widgets

## Overview

Widgets are the building blocks of M3L, defining the structure and functionality of an application’s user interface. M3L provides a set of **standard widgets** for common use cases and supports **custom widgets** for developers who need unique layout flexibility. Each widget can manage its state, ensuring interactivity and responsiveness, while the styling and feel are always controlled by GSS to maintain consistency.

---

## Standard Widgets

M3L includes a comprehensive library of standard widgets that cover a wide range of UI needs. These widgets come with required and optional fields, allowing developers to customize their behavior and appearance.

---

### Examples of Standard Widgets

#### **1. Asset Grid**

- **Description**: Displays a grid of assets for exploration or purchase.
- **Required Fields**:
    - `type`: Defines the widget type (`asset_grid`).
    - `resources`: Points to the data source for the grid.
- **Optional Fields**:
    - `update_on`: Specifies events that trigger content updates (e.g., `filter_change`).

**Example:**

```toml
[[layout.container.content]]
type = "asset_grid"
intention = "browse"
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" }
]
update_on = "filter_change"
```

---

#### **2. Carousel**

- **Description**: Cycles through images or content items, often used for promotions or highlights. A carousel can be as simple as a set of rotating images or as complex as a collection of cards with images, descriptions, and buttons.
- **Required Fields**:
    - `type`: Defines the widget type (`carousel`).
    - `resources`: Points to the content source.

**Example:**

```toml
[[layout.container.content]]
type = "carousel"
resources = [
    { link = "@Undline/assets/promotions.toml", type = "carousel_items" }
]
```

---

#### **3. Tooltip**

- **Description**: Provides contextual information when a user hovers or focuses on an element.
- **Required Fields**:
    - `type`: Defines the widget type (`tooltip`).
    - `description`: The text to display.

**Example:**

```toml
[[layout.container.content]]
type = "tooltip"
description = "Hover here for more information."
```

---

#### **4. Navigation Menu**

- **Description**: Creates a menu for navigating between sections or pages.
- **Required Fields**:
    - `type`: Defines the widget type (`nav_menu`).
    - `items`: A list of menu options and their associated links.

**Example:**

```toml
[[layout.container]]
type = "nav_menu"
items = [
    { text = "Home", resource = "@Undline/home.m3l" },
    { text = "Products", resource = "@Undline/products.m3l" }
]
```

---

## Custom Widgets

Custom widgets allow developers to modify the **layout** and **structure** of a widget when standard widgets do not meet their needs. **Styling and interaction rules remain strictly controlled by GSS**, ensuring consistency across applications.

### Defining a Custom Widget

Custom widgets can be added to M3L by specifying a new `type` and associating it with custom functionality in the application.

**Example:**

```toml
[[layout.container.content]]
type = "custom_widget"
intention = "analyze"
resources = [
    { link = "CustomChain://Analytics/Data" }
]
```

- **Important Note**: Custom widgets cannot redefine styles or interactions; those are handled in GSS.

---

## State Management

M3L supports defining and managing widget states, allowing developers to create interactive and responsive UIs. States can be used to indicate a widget’s current status, such as:

- **Focus**: The widget is currently in use or selected.
- **Disabled**: The widget is inactive and cannot be interacted with.
- **Highlighted**: The widget is visually emphasized.

### Defining States in M3L

Widget states are defined using the `state` property within a widget configuration.

**Example:**

```toml
[[layout.container.content]]
type = "button"
state = { focus = true, disabled = false, highlighted = true }
order = 1
```

- **Order Parameter**: The `order` parameter specifies the tab order for widgets, allowing seamless navigation for keyboard and controller users.

---

## Widget Reference Library

For a comprehensive list of all standard widgets, including their required and optional fields, see the **Widget Reference** section in the Appendix. This includes detailed descriptions, examples, and supported parameters for each widget type.

---

## Summary

Widgets in M3L are highly flexible, offering both standard components for common use cases and the ability to define custom ones. State management ensures that UIs remain interactive and responsive, while the `order` parameter provides enhanced navigation capabilities. By leveraging M3L’s widget system, developers can create modular, dynamic, and engaging applications tailored to user needs while maintaining a consistent look and feel through GSS.

---

# Accessibility

## Overview

Accessibility ensures that all users, regardless of their abilities or the devices they use, can effectively interact with applications built using M3L and GSS. By adhering to best practices, developers can create inclusive applications that meet usability standards while leveraging the flexibility of M3L and the styling power of GSS.

---

## Best Practices for Creating Accessible GSS Files

1. **Focus Management**:
    - Define clear focus states for interactive widgets using the `focus` property in M3L and corresponding visual cues in GSS.
    - Ensure focusable elements have an appropriate `order` to facilitate logical keyboard and controller navigation.

**Example:**

```toml
[[layout.container.content]]
type = "button"
state = { focus = false, disabled = false, highlighted = false }
order = 2
```

```toml
[button.focus]
border-color = "#007BFF"
border-width = "2px"
background-color = "#f0f8ff"
```

---

2. **Tooltips for Contextual Guidance**:
    - Include tooltips for elements that require additional explanation.
    - Use GSS to style tooltips for readability and ensure they are triggered appropriately based on user interaction (e.g., hover, focus).

**Example:**

```toml
[[layout.container.content]]
type = "tooltip"
description = "Press this button to confirm your action."
```

```toml
[tooltip]
background-color = "#000"
color = "#fff"
padding = "8px"
border-radius = "5px"
font-size = "12px"
trigger.help.mouse = "on hover"
trigger.help.focus = "on focus"
```

---

3. **Color Contrast**:
    - Ensure sufficient contrast between text and background colors to meet WCAG standards.
    - Use high-contrast modes for users with visual impairments.

**Example:**

```toml
[global]
body.background-color = "#ffffff"
body.color = "#000000"

[high_contrast]
body.background-color = "#000000"
body.color = "#ffffff"
```

---

4. **Keyboard and Controller Navigation**:
    - Use the `order` parameter to create logical navigation flows.
    - Ensure all interactive elements are reachable using a keyboard or controller.

**Example:**

```toml
[[layout.container.content]]
type = "nav_menu"
items = [
    { text = "Home", resource = "@Undline/home.m3l", order = 1 },
    { text = "Products", resource = "@Undline/products.m3l", order = 2 }
]
```

---

## Examples of Accessible Implementations

### **1. Tooltips and Focus Management**

Tooltips can provide additional context for users while maintaining visual clarity.

```toml
[[layout.container.content]]
type = "tooltip"
description = "Click here to learn more."
state = { focus = false }
```

```toml
[tooltip.focus]
border-color = "#00ff00"
background-color = "#333"
font-size = "14px"
```

### **2. High Contrast Modes**

Enable users to toggle between standard and high-contrast modes.

```toml
[[layout.container.content]]
type = "toggle"
intention = "toggle"
resources = [
    { link = "Settings://ToggleHighContrast" }
]
```

```toml
[high_contrast]
body.background-color = "#000"
body.color = "#fff"
```

---

## Future Integration

While M3L and GSS natively support accessibility features, co-chains like **Mimic** can enhance usability by providing contextual guidance or advanced interaction capabilities. For example, Mimic can analyze widget states and user behavior to suggest actions or streamline workflows.

Developers can also integrate any co-chain into the resource list of a widget to extend usability features. This ensures M3L remains open and adaptable for advanced environments, giving developers the freedom to innovate.

**Example with Multiple Co-Chains:**

```toml
[[layout.container.content]]
type = "tooltip"
description = "Click here for more information."
resources = [
    { link = "Mimic://Help/tooltip_assistance" }, # Mimic for AI guidance
    { link = "CustomChain://Usability/Help" }     # Custom co-chain for usability
]
```

---

## Summary

Accessibility in M3L and GSS is achieved through focus management, contextual guidance with tooltips, proper color contrast, and logical navigation flows. By following these best practices and leveraging co-chains like Mimic, developers can create applications that are inclusive, user-friendly, and compliant with accessibility standards while maintaining the flexibility to innovate with their own co-chains.

---

# Examples

## Overview

This section provides complete examples of M3L and GSS files to demonstrate how to build functional and visually consistent applications. Each example includes a step-by-step walkthrough to help developers understand the integration of widgets, co-chains, and styling. Additionally, a graphical editor is planned for the future to support developers who prefer visual tools over textual editing.

---

## Example 1: Marketplace with Carousel, Asset Grid, and Error Handling

### M3L File

```toml
[meta]
title = "Marketplace"
description = "A showcase of assets available for purchase."
author = "@Undline"

[rating]
classification = "Everyone"
public_approval = 95
content_type = "marketplace"

[layout]
[[layout.container]]
id = "header"
type = "nav_menu"
items = [
    { text = "Home", resource = "@Undline/home.m3l", order = 1 },
    { text = "Products", resource = "@Undline/products.m3l", order = 2 }
]

[[layout.container]]
id = "hero"
type = "carousel"
resources = [
    { link = "@Undline/assets/promotions.toml", type = "carousel_items" }
]

[[layout.container]]
id = "main"
type = "asset_grid"
intention = "browse"
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" }
]
update_on = "filter_change"

[[layout.container]]
id = "error"
type = "error_widget"
description = "Unable to load content. Please try again later."
```

### GSS File

```toml
[global] # Global styles for the entire page
body.font-family = "Roboto, sans-serif"
body.background-color = "#ffffff"
body.color = "#333"
body.font-size = "16px" # Root font size, used for rem units

[nav_menu] # Styles for the navigation menu
background-color = "#007BFF"
color = "#fff"
padding = "10px"

[carousel] # Styles for the carousel
item.margin = "1rem" # Using rem for consistent spacing
item.border-radius = "0.5rem"
item.shadow = "0 4px 6px rgba(0, 0, 0, 0.1)"
animation.type = "slide" # Adding an animation for carousel rotation
animation.duration = "2s"
animation.easing = "ease-in-out"

[asset_grid] # Styles for the asset grid
item.padding = "1.5em" # Using em for spacing relative to the font size of the grid item
item.border = "1px solid #ddd"
item.background-color = "#f9f9f9"
item.hover.border-color = "#007BFF"

[loading] # Sub-widget for loading states
animation.type = "fade" # Simple fade-in animation for loading state
animation.duration = "1s"
animation.easing = "linear"
content = "Loading..."

[error_widget] # Styles for error notifications
background-color = "#ffcccc"
color = "#900"
padding = "1em"
border-radius = "0.5rem"
font-size = "1rem"
position = "banner" # Options: banner, popup, toast
```

---

## Example 2: Simple Static Content Page with Hero Section

### M3L File

```toml
[meta]
title = "Welcome"
description = "A simple static page with a hero section."
author = "@Undline"

[rating]
classification = "Everyone"
public_approval = 90
content_type = "static_page"

[layout]
[[layout.container]]
id = "hero"
type = "hero_section"
header = "Welcome to Our Platform"
subheader = "Explore the best we have to offer."
cta_button = { text = "Get Started", resource = "@Undline/get_started.m3l" }
muted_button = { text = "Learn More", resource = "@Undline/learn_more.m3l" }

[[layout.container]]
id = "footer"
type = "static_content"
source = "@Undline/assets/footer_content.md"
```

### GSS File

```toml
[global] # Global styles for the entire page
body.font-family = "Arial, sans-serif"
body.background-color = "#f4f4f4"
body.color = "#333"
body.font-size = "16px" # Setting root font size for rem units

[hero_section] # Styles for the hero section
header.font-size = "2.5rem" # Using rem for scalable typography
header.color = "#007BFF"
subheader.font-size = "1.5rem"
subheader.color = "#555"
cta_button.background-color = "#007BFF"
cta_button.color = "#fff"
cta_button.padding = "0.625rem 1.25rem"
cta_button.border-radius = "0.3125rem"
muted_button.background-color = "#ddd"
muted_button.color = "#333"
muted_button.padding = "0.625rem 1.25rem"
muted_button.border-radius = "0.3125rem"

[footer] # Styles for the footer section
background-color = "#333"
color = "#fff"
padding = "1.25rem"
font-size = "0.9rem"
```

---

## Walkthrough: Building a Marketplace Page

### Step 1: Define the M3L Structure

1. Start with the metadata section to define the page’s purpose and audience.
2. Add layout containers for the navigation menu, carousel, and asset grid.
3. Specify resource links for dynamic content like the asset grid and promotions.
4. Include an error widget to handle content loading issues.

**Example Metadata and Layout:**

```toml
[meta]
title = "Marketplace"
description = "A showcase of assets available for purchase."
author = "@Undline"

[layout]
[[layout.container]]
id = "header"
type = "nav_menu"
items = [
    { text = "Home", resource = "@Undline/home.m3l", order = 1 },
    { text = "Products", resource = "@Undline/products.m3l", order = 2 }
]
```

---

### Step 2: Style the Page Using GSS

1. Define global styles for fonts and background colors.
2. Customize the appearance of each widget (e.g., `nav_menu`, `carousel`, `asset_grid`).
3. Add animations to enhance interactivity, such as carousel rotations or loading indicators.
4. Style the error widget to ensure visibility and usability.
5. Incorporate **em** and **rem** units for scalable and responsive designs.

**Example GSS Styles:**

```toml
[global] # Global styles
body.font-family = "Roboto, sans-serif"
body.background-color = "#ffffff"
body.color = "#333"
body.font-size = "16px"

[carousel] # Adding rotation animation
item.margin = "1rem"
animation.type = "slide"
animation.duration = "2s"
animation.easing = "ease-in-out"

[error_widget] # Error widget styling
background-color = "#ffcccc"
color = "#900"
padding = "1em"
border-radius = "0.5rem"
position = "popup"
```

---

### Step 3: Test and Iterate

1. Preview the page using the M3L engine to ensure dynamic content loads correctly.
2. Adjust styles, animations, and layout as needed for responsiveness and aesthetics.
3. Simulate error states to verify that the error widget behaves as expected.

---

## Summary

These examples demonstrate how M3L and GSS work together to create dynamic, styled, and accessible pages. Future graphical editors will simplify the process further, making it even easier for developers to build pages visually. By following these examples and walkthroughs, developers can leverage the full power of M3L, GSS, and co-chain integration to create robust applications.

---

# Event Handling

## Overview

Event handling in M3L and GSS allows developers to manage system and user-triggered events with precision and flexibility. These events include five primary types: **error**, **warning**, **information**, **confirmation**, and **notification**. Each event type has unique characteristics and can be styled to align with application design goals. Developers can also define how these events are triggered and implement fallback behaviors to ensure a seamless user experience.

---

## Event Types and Use Cases

### 1. **Error Events**

- **Purpose**: To inform users of a critical issue that requires immediate attention.
- **Common Uses**:
    - Failed form submissions.
    - Network connectivity issues.
    - Invalid data format received from a co-chain.

**Example M3L:**

```toml
[[layout.container.content]]
type = "error_widget"
description = "Unable to connect to the server. Please try again later."
```

**Example GSS:**

```toml
[error_widget]
background-color = "#ffcccc"
color = "#900"
padding = "1em"
border-radius = "0.5rem"
position = "popup"
font-size = "1rem"
```

---

### 2. **Warning Events**

- **Purpose**: To alert users about potential issues or risks.
- **Common Uses**:
    - Unsaved changes warnings.
    - Low disk space alerts.

**Example M3L:**

```toml
[[layout.container.content]]
type = "warning_widget"
description = "You have unsaved changes. Do you want to continue?"
```

**Example GSS:**

```toml
[warning_widget]
background-color = "#fff4cc"
color = "#856404"
padding = "1em"
border-radius = "0.5rem"
position = "banner"
font-size = "1rem"
```

---

### 3. **Information Events**

- **Purpose**: To provide users with non-critical updates or details.
- **Common Uses**:
    - Successful actions.
    - General system notifications.

**Example M3L:**

```toml
[[layout.container.content]]
type = "info_widget"
description = "Your profile has been updated successfully."
```

**Example GSS:**

```toml
[info_widget]
background-color = "#d1ecf1"
color = "#0c5460"
padding = "1em"
border-radius = "0.5rem"
position = "toast"
font-size = "1rem"
```

---

### 4. **Confirmation Events**

- **Purpose**: To request user approval for an action.
- **Common Uses**:
    - Deleting an item.
    - Submitting a payment.

**Example M3L:**

```toml
[[layout.container.content]]
type = "confirmation_widget"
description = "Are you sure you want to delete this item?"
cta_button = { text = "Yes", action = "delete_item" }
muted_button = { text = "No", action = "cancel" }
```

**Example GSS:**

```toml
[confirmation_widget]
background-color = "#e9ecef"
color = "#495057"
padding = "1em"
border-radius = "0.5rem"
position = "popup"
font-size = "1rem"
```

---

### 5. **Notification Events**

- **Purpose**: To keep users informed about background processes or general updates.
- **Common Uses**:
    - Download progress updates.
    - System maintenance reminders.

**Example M3L:**

```toml
[[layout.container.content]]
type = "notification_widget"
description = "Your download is 50% complete."
```

**Example GSS:**

```toml
[notification_widget]
background-color = "#e2e3e5"
color = "#383d41"
padding = "1em"
border-radius = "0.5rem"
position = "toast"
font-size = "1rem"
```

---

## Event Triggers and Widget-Specific Behavior

### Timeout Property

Developers can define a `timeout` property in the M3L file for widgets that interact with co-chains. If the co-chain does not respond within the specified time, the widget triggers a connection error. The default timeout is 44 seconds if not explicitly defined.

**Example M3L with Timeout:**

```toml
[[layout.container.content]]
type = "asset_grid"
intention = "browse"
resources = [
    { link = "SQeeL://Auction_House/assets.db", type = "grid_items" }
]
timeout = 30 # Maximum wait time in seconds
```

**Example GSS for Timeout Handling:**

```toml
[asset_grid.loading]
animation.type = "fade"
animation.duration = "1s"
content = "Loading assets..."

[asset_grid.error]
description = "Unable to load assets within the allowed time."
icon = "timeout_error.png"
position = "banner"
```

---

### Widget-Driven Event States

Events are most commonly triggered by widgets based on their interactions with co-chains. For example:

- **Asset View Widget**: If the widget fails to receive data within the timeout, it triggers a connection error.
- **Form Widget**: Missing or invalid data results in an error returned by the co-chain.

**Example: Form Validation Error**

```toml
[form.error]
field-highlight = "#ffdddd"
dialog.message = "Phone number is required."
dialog.button = { text = "Fix Now", action = "focus_phone_field" }
```

### Data Parsing Error

If the data retrieved from a co-chain is in an invalid format, the widget attempts a retry. If the issue persists, an error is triggered, and a message is optionally sent back to the co-chain.

**Example:**

```toml
[asset_grid.error]
description = "Invalid data format received. Please contact support."
icon = "data_error.png"
position = "popup"
```

---

### Standardized Error Format

Co-chains are expected to return errors in a standardized format to ensure consistent handling across widgets. The required fields include:

- **Event Type**: Specifies the category (e.g., error, warning).
- **Event Name (Header)**: A concise title for the event.
- **Description**: A detailed explanation of the issue.

### Optional Fields

- **Icons or Images**: To visually represent the event.
- **Buttons**: To allow users to take corrective actions directly.

**Example of Standardized Error Response**:

```json
{
    "event_type": "error",
    "event_name": "Connection Timeout",
    "description": "Connection timed out while fetching assets.",
    "icon": "timeout_error.png",
    "buttons": [
        { "text": "Retry", "action": "retry_connection" }
    ]
}
```

---

## Best Practices for Fallback Behavior

1. **Default Styling**: Always provide default styles for event widgets to ensure usability if custom styles are missing.
2. **Graceful Degradation**: Ensure that events still display essential information even if advanced features fail.
3. **Retry Mechanisms**: Attempt automatic retries for transient issues, such as corrupted data or temporary network errors.
4. **Accessibility**: Ensure that event widgets are focusable and provide appropriate ARIA roles or labels for screen readers.

---

## Summary

Event handling in M3L and GSS is a robust system for managing user interactions and system notifications. By leveraging event types, dynamic triggers, and fallback behaviors, developers can create clear and responsive interfaces that keep users informed and engaged while maintaining accessibility and consistency.

---

# Future Proofing

## Overview

M3L and GSS are designed with extensibility in mind to ensure that applications can adapt to future technologies and user needs. By incorporating placeholder fields, encouraging modular design, and planning for advanced features like VR and BMI (brain-machine interface), the system remains flexible and robust over time.

---

## Placeholder Fields for Co-Chains

To ensure compatibility with future co-chains and advanced functionality, placeholder fields can be defined in the M3L file. These placeholders allow for seamless integration of upcoming features without requiring major changes to existing files. Placeholders should remain as `0` or `""` to indicate they are not yet in use.

**Example Placeholder for Mimic Integration:**

```toml
[meta]
mimic_content_ID = "" # Placeholder when Mimic is not yet live
```

**Example When Mimic is Live:**

```toml
[meta]
mimic_content_ID = "Mimic://Auction House/content ID" # Mimic integration for live contextual information
```

By maintaining placeholder fields, developers can future-proof their M3L files without risking malicious or unintended behavior. Only when explicitly updated should these fields hold active values.

---

## Suggestions for Extending M3L and GSS

### **1. Virtual Reality (VR) Support**

- **Goal**: Enable immersive user experiences by integrating VR-specific widgets and interactions.
- **Approach**:
    - Introduce spatial properties like `z-order` in GSS to manage depth and layering of widgets.
    - Expand M3L to support VR-specific attributes for enhanced 3D interactions.

**Possible Features:**

- `z-order` to control widget depth placement.
- Interaction models for VR controllers.

---

### **2. Brain-Machine Interface (BMI) Support**

- **Goal**: Facilitate hands-free interactions using brainwave-driven commands.
- **Approach**:
    - Extend M3L intents to include thought-based actions (e.g., `think_back` for page navigation).
    - Allow GSS to define visual feedback for BMI-triggered interactions.

**Possible Features:**

- Thought commands mapped to intents like `think_forward` or `think_select`.
- Integration of focus indicators tied to brainwave activity.

---

## High-Order Widget Compatibility

To ensure future high-order widgets remain compatible with existing GSS files, the design must include a listing of smaller widgets within each high-order widget. This ensures that:

1. **Backward Compatibility**: Widgets retain basic functionality and styling, even if the GSS file predates the widget.
2. **Comprehensive Styling**: New GSS files can fully implement styling for all widget components, improving user experience and visual consistency.
3. **Version Awareness**: If the M3L engine does not recognize a new high-order widget type, it will throw an error and attempt to fetch an updated version of the engine to interpret it.

**Example High-Order Widget Definition:**

```toml
[[layout.container.content]]
type = "dashboard"
components = ["graph", "text_editor", "button"]
```

**Example GSS Implementation:**

```toml
[dashboard]
background-color = "#f5f5f5"

[dashboard.graph]
border = "1px solid #ddd"

[dashboard.text_editor]
font-family = "Monospace"

[dashboard.button]
background-color = "#007BFF"
color = "#fff"
```

---

## Versioning in M3L Files

Every M3L file should include a version field in the `meta` table to indicate the version of M3L it was written with. This ensures compatibility checks and proper handling by the M3L engine.

**Example Meta Table with Version:**

```toml
[meta]
title = "Example Page"
author = "@Undline"
version = "2025.01.05.0" # Format: YYYY.MM.DD.subversion
```

---

## Auction House Promotion for Comprehensive GSS Files

GSS files that fully implement all available widgets in the current version of M3L will receive greater visibility in the Auction House. This ensures that developers prioritize keeping their GSS files updated and fully compatible with the latest features. Older GSS files that do not implement newer widgets will be ranked lower in search results to encourage adoption of comprehensive, future-proof designs.

**Example Note in Auction House:**

- **Featured GSS File**: "Cyberpunk Theme - Supports All Widgets"
    - Compatibility: Full
    - Accessibility: WCAG Compliant
    - Rating: 95%

---

## Summary

Future-proofing in M3L and GSS is achieved through thoughtful design choices, such as placeholder fields for co-chains, modular high-order widgets, versioning in M3L files, and incentives for comprehensive GSS files. By planning for advancements like VR and BMI support, the system remains adaptable and forward-looking, empowering developers to create applications that stand the test of time while maintaining strict security and consistency.

---
---

# Appendix: Widgets

## Overview
This appendix provides a comprehensive listing of all widgets supported by M3L and GSS, including their types, examples, and styling options. Widgets are categorized into **low-level widgets** (basic building blocks). Each widget includes a detailed description, example usage in M3L, and corresponding styling in GSS to help developers understand its purpose and implementation. 

**Note**: All setting and value entries are **not case-sensitive**; they are converted to lowercase during processing, ensuring consistent handling and easing development.

---

## Low-Level Widgets

### **Frame Widgets**
Frames are essential for structuring layouts in M3L. They act as containers that define how child widgets are positioned and aligned. Frames come in various types, allowing developers to create responsive, flexible, and complex UIs.

#### **Frame vs. Window**
- **Frame**: Manages the layout of widgets within an application.
- **Window**: Simulates an application environment, allowing developers to preview new GSS styles or UI designs. It provides an isolated space for testing and experimentation.

---

### **Frame Types**

#### **1. Grid Frame**
- Organizes widgets into rows and columns, providing structured layouts for dashboards, forms, or content grids.

**Fields**:
| **Field**    | **Description**                                               | **Example**           |
|--------------|---------------------------------------------------------------|-----------------------|
| `rows`       | Number of rows in the grid.                                   | `rows = 3`            |
| `columns`    | Number of columns in the grid.                                | `columns = 3`         |
| `gap`        | Spacing between rows and columns.                             | `gap = "10px"`        |
| `alignment`  | Aligns widgets in the grid (start, center, end, stretch).     | `alignment = "center"`|
| `margin`     | Spacing around the grid.                                      | `margin = "10px"`     |
| `padding`    | Spacing inside the grid container.                            | `padding = "5px"`     |
| `z_order`    | Stacking order of widgets within the grid (2D layering).      | `z_order = 1`         |
| `x`, `y`, `z`| Position offsets for the grid relative to its container. **Note**: `z` is reserved for future use and currently ignored. | `x = "20px", y = "10px", z = "0"` |

**Example**:
```toml
[[layout.container.content]]
type = "frame"
frame_type = "grid"
rows = 2
columns = 3
gap = "10px"
alignment = "center"
margin = "15px"
padding = "10px"
x = "0"
y = "0"
z = "0"

children = [
    {
        type = "button",
        label = "Submit"
    }
]
```

---

#### **2. Relative Frame**
- Positions widgets based on an anchor point, making it useful for placing elements near each other or aligning them dynamically.

**Fields**:
| **Field**      | **Description**                                            | **Example**            |
|----------------|------------------------------------------------------------|------------------------|
| `anchor`       | Specifies the reference point for positioning (top-left, center). | `anchor = "top-left"`  |
| `offset_x`     | Horizontal offset from the anchor point.                   | `offset_x = "20px"`    |
| `offset_y`     | Vertical offset from the anchor point.                     | `offset_y = "10px"`    |
| `z_order`      | Stacking order for widgets in the frame.                   | `z_order = 2`          |
| `x`, `y`, `z`  | Position offsets for the entire frame. **Note**: `z` is reserved for future use and currently ignored. | `x = "0", y = "0", z = "0"` |
| `margin`       | Spacing around the relative frame.                         | `margin = "10px"`      |
| `padding`      | Spacing inside the relative frame container.               | `padding = "5px"`      |

**Example**:
```toml
[[layout.container.content]]
type = "frame"
frame_type = "relative"
anchor = "top-left"
offset_x = "20px"
offset_y = "10px"
x = "0"
y = "0"
z = "0"
margin = "10px"
padding = "5px"

children = [
    {
        type = "image",
        src = "@Undline/assets/logo.png"
    }
]
```

---

#### **3. Absolute Frame**
- Allows precise placement of widgets using x, y, and z coordinates, ideal for pixel-perfect designs.

**Fields**:
| **Field**      | **Description**                                                | **Example**          |
|----------------|----------------------------------------------------------------|----------------------|
| `x`, `y`, `z`  | Exact coordinates for placing widgets within the frame. **Note**: `z` is reserved for future use and currently ignored. | `x = "50px", y = "100px", z = "1"` |
| `z_order`      | Stacking order for overlapping widgets.                        | `z_order = 1`        |
| `margin`       | Spacing around the frame.                                      | `margin = "10px"`    |
| `padding`      | Spacing inside the frame container.                            | `padding = "5px"`    |

**Example**:
```toml
[[layout.container.content]]
type = "frame"
frame_type = "absolute"
x = "0"
y = "0"
z = "0"
margin = "10px"
padding = "5px"

children = [
    {
        type = "text",
        content = "Welcome to M3L!",
        x = "50px",
        y = "100px",
        z = "1"
    }
]
```

---

#### **4. Flex Frame**
- Aligns widgets along a single axis (row or column) with options for wrapping, spacing, and alignment.

**Fields**:
| **Field**          | **Description**                                            | **Example**                |
|--------------------|------------------------------------------------------------|----------------------------|
| `direction`        | Specifies the axis for alignment (row or column).          | `direction = "row"`        |
| `wrap`             | Enables wrapping of widgets if space is insufficient.      | `wrap = true`              |
| `justify_content`  | Distributes space between widgets (start, center, end).    | `justify_content = "space-around"` |
| `align_items`      | Aligns widgets along the perpendicular axis.               | `align_items = "center"`   |
| `margin`           | Spacing around the frame.                                  | `margin = "10px"`          |
| `padding`          | Spacing inside the frame container.                        | `padding = "5px"`          |

**Example**:
```toml
[[layout.container.content]]
type = "frame"
frame_type = "flex"
direction = "row"
wrap = true
justify_content = "space-around"
align_items = "center"
margin = "15px"
padding = "10px"

children = [
    {
        type = "button",
        label = "Buy Now"
    }
]
```

---

### **Nesting Frames**
Frames can be nested to create advanced layouts. For example, a Flex Frame might contain a Grid Frame, which itself contains Relative Frames for individual widget placement. For deeply nested layouts, it is recommended to use external files for `children` after three levels of nesting.

**Example Hybrid**:
```toml
[[layout.container.content]]
type = "frame"
frame_type = "flex"
direction = "row"
wrap = true
justify_content = "space-around"

children = [
    {
        type = "frame",
        frame_type = "grid",
        rows = 2,
        columns = 3,
        gap = "5px",
        children = "@path/to/nested_children.gss"
    }
]
```

---

### **Key Recommendations**
- Use `z` for future 3D implementation. It is ignored for now but ensures compatibility with future features.
- Leverage nested frames for complex layouts and modular designs.
- Combine frame types (e.g., Grid within Flex) for maximum flexibility and responsiveness.
- For deeply nested layouts, use external files for `children` to enhance readability and maintainability.

---

### **Button Widget**

Buttons are versatile widgets that trigger actions or navigate users through the interface. They support multiple predefined types and rich customization options, including animations and interactive effects.

---

### **Button Types**
1. **Primary Button (CTA)**:
   - Highlights the main action for users (e.g., "Submit" or "Proceed").
2. **Secondary Button (Muted)**:
   - Used for supporting or less critical actions (e.g., "Cancel" or "Go Back").
3. **Image Button**:
   - Uses an image as the button surface while retaining full button functionality.
4. **Confirmation Button**:
   - Requires an additional step to confirm the action (e.g., click-and-hold).
5. **Toggle Button**:
   - Allows switching between two states, such as ON/OFF.
6. **Floating Action Button**:
   - A circular button designed for key actions with optional drag functionality.

---

### **Core Fields**
| **Field**       | **Description**                                                                 | **Example**                            |
|-----------------|---------------------------------------------------------------------------------|----------------------------------------|
| `label`         | Text displayed on the button (if applicable).                                   | `label = "Submit"`                     |
| `icon`          | Path to the icon or image for the button surface.                               | `icon = "@Undline/assets/icon.svg"`    |
| `type`          | Specifies the button type (`primary`, `secondary`, `icon`, `confirmation`, `toggle`, `floating`). | `type = "confirmation"`                |
| `action`        | Action triggered when the button is clicked.                                    | `action = "purchase"`                  |
| `target`        | Target resource or page for the action (if applicable).                         | `target = "@Undline/api/buy"`          |
| `tooltip`       | Text displayed when hovering over the button.                                   | `tooltip = "Click to Purchase"`        |
| `confirmation`  | Enables a two-step confirmation process.                                        | `confirmation = true`                  |
| `click_and_hold`| Triggers an action after holding the button for a set duration (in ms).          | `click_and_hold = 2000`                |
| `disabled`      | Disables the button, preventing interaction.                                    | `disabled = true`                      |
| `loading`       | Shows a loading animation when the button is pressed until the action resolves. | `loading = true`                       |
| `state`         | Defines the button’s current state (`default`, `active`, `focused`).            | `state = "default"`                    |
| `boundary`      | Defines the boundary area for floating buttons.                                | `boundary = { top = "10px", bottom = "10px", left = "10px", right = "10px" }` |
| `font`          | Defines font properties such as type and size.                                 | `font = { family = "Arial", size = "1rem" }` |
| `background`    | Supports gradient colors or images for the button background.                  | `background = { type = "gradient", colors = ["#007BFF", "#0056b3"] }` |
| `border`        | Defines the border style, width, and color.                                     | `border = "1px solid #007BFF"`         |
| `border_radius` | Rounds the corners of the button.                                               | `border_radius = "5px"`                |
| `shadow`        | Adds drop shadow effects to the button.                                         | `shadow = { color = "#000", blur = "5px", offset_x = "2px", offset_y = "2px" }` |

---

### **Animation Parameters**
Animations enhance user experience by providing visual feedback. Designers can use predefined animations or define custom ones.

| **Parameter**       | **Description**                                              | **Example**                               |
|---------------------|--------------------------------------------------------------|-------------------------------------------|
| `entrance.animation`| Defines the animation when the button appears.               | `entrance.animation = "fade-in"`          |
| `hover.animation`   | Specifies the animation when the button is hovered over.     | `hover.animation = "scale-up"`            |
| `click.animation`   | Defines the animation triggered on click or interaction.     | `click.animation = "progress-fill"`       |
| `exit.animation`    | Specifies the animation when the button exits.               | `exit.animation = "fade-out"`             |
| `duration`          | Duration of the animation (in seconds).                      | `duration = "1s"`                         |
| `timing_function`   | Specifies easing for the animation.                          | `timing_function = "ease-in-out"`         |
| `custom_animation`  | Allows developers to define their animations using custom logic. | `custom_animation = { steps = [{ opacity = "0" }, { opacity = "1" }], duration = "2s" }` |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "button"
label = "Submit"
type = "confirmation"
action = "purchase"
target = "@Undline/api/buy"
tooltip = "Hold to Confirm Purchase"
confirmation = true
click_and_hold = 2000
boundary = { top = "10px", bottom = "10px", left = "10px", right = "10px" }

font = { family = "Arial", size = "1rem" }
background = { type = "gradient", colors = ["#007BFF", "#0056b3"] }
shadow = { color = "#000", blur = "5px", offset_x = "2px", offset_y = "2px" }
border = "1px solid #007BFF"
border_radius = "5px"

on_click = [
    { intent = "start_purchase", target = "@Undline/api/buy" }
]
```

---

### **Example GSS Implementation**
```toml
[button.primary]
background-color = "#007BFF"
color = "#FFFFFF"
border = "1px solid #007BFF"
border-radius = "5px"
padding = "10px 20px"
font-family = "Arial, sans-serif"
font-size = "1rem"

[button.primary.hover]
background-color = "#0056b3"

[button.primary.animation]
entrance.animation = "fade-in"
hover.animation = "scale-up"
click.animation = "progress-fill"
exit.animation = "fade-out"
duration = "1s"
timing_function = "ease-in-out"

[button.floating]
background = { type = "gradient", colors = ["#FF5733", "#FF4500"] }
color = "#FFFFFF"
border-radius = "50%"
shadow.color = "#000"
shadow.blur = "10px"
position = { x = "50px", y = "50px" }
boundary = { top = "0px", bottom = "0px", left = "0px", right = "0px" }

[button.floating.draggable]
cursor = "grab"

[button.custom_animation]
steps = [
    { opacity = "0" },
    { opacity = "1" }
]
duration = "2s"
```

---

### **Text Widget**

The Text Widget serves as a fundamental low-level component for displaying and styling text. It supports headers, paragraphs, lists, highlighter text, hyperlinks, tables, and breaks, with rich customization options for styling, interactivity, and animations.

---

### **Core Text Types**
1. **Headers (H1–H5)**:
   - Structured headings for content hierarchy.
   - Ranges from large, primary titles (H1) to smaller subheadings (H5).
2. **Paragraph Text**:
   - Used for general content, such as articles or descriptive text.
3. **Lists**:
   - **Ordered Lists**: Numbered sequences for instructions or steps.
   - **Unordered Lists**: Bullet points for non-sequential items.
4. **Highlighter Text**:
   - Emphasizes specific words or phrases with a background color.
5. **Hyperlinks**:
   - Inline or block-level links to other pages or resources, with default tooltips displaying the link destination.
6. **Tables**:
   - Used to display structured data in rows and columns.
   - Supports header rows, alignment, and custom styling for each cell.
7. **Breaks (Lines)**:
   - Horizontal rules or decorative breaks to separate sections of content.

---

### **Proposed Fields**
| **Field**       | **Description**                                                            | **Example**                                    |
|-----------------|----------------------------------------------------------------------------|-----------------------------------------------|
| `type`          | Specifies the text type (`header`, `paragraph`, `list`, `highlighter`, `link`, `table`, `break`). | `type = "header"`                             |
| `content`       | The actual text to be displayed.                                           | `content = "Welcome to M3L!"`                 |
| `style`         | Indicates the text style (e.g., H1-H5, or `paragraph`, `ordered`, etc.).   | `style = "H1"`                                |
| `href`          | Specifies the hyperlink destination (only for `type = "link"`).            | `href = "@Undline/page.m3l"`                  |
| `highlight`     | Enables background highlighting with a specified color (for highlighter).  | `highlight = "#FFFF00"`                       |
| `list_style`    | Defines the marker style for lists (bullet, number, Roman numeral).         | `list_style = "bullet"`                       |
| `font`          | Specifies the font family and size.                                        | `font = { family = "Verdana", size = "1rem" }` |
| `alignment`     | Sets text alignment (e.g., left, center, right, justify).                  | `alignment = "center"`                        |
| `line_spacing`  | Adjusts the spacing between lines of text.                                | `line_spacing = "1.5"`                         |
| `letter_spacing`| Adjusts the spacing between letters.                                       | `letter_spacing = "0.1em"`                    |
| `selectable`    | Allows the text to be selected for copying.                                | `selectable = true`                            |
| `table_data`    | Defines the structure and content of a table (only for `type = "table"`). | `table_data = [ { row = ["Name", "Age"] }, { row = ["Alice", "30"] } ]` |
| `line_style`    | Specifies the appearance of a break line (only for `type = "break"`).     | `line_style = { color = "#333", thickness = "2px" }` |
| `animations`    | Defines enter/exit animations for text elements.                          | `animations = { enter = "fade-in", exit = "fade-out", duration = "1s" }` |

---

### **Intents and Events**
| **Intent/Event** | **Description**                                                                 | **Example**                                   |
|------------------|---------------------------------------------------------------------------------|-----------------------------------------------|
| `on_click`       | Triggered when the text (e.g., a hyperlink) is clicked.                        | `on_click = [{ navigate = "@Undline/page.m3l" }]` |
| `on_hover`       | Triggered when the text is hovered over (e.g., to show a tooltip).             | `on_hover = [{ tooltip = "Learn more at this link." }]` |
| `on_focus`       | Triggered when the text gains focus (e.g., via Tab navigation).                 | `on_focus = [{ animate = "underline" }]`     |

---

### **GSS Styling Parameters**
| **Parameter**      | **Description**                                                            | **Example**                                   |
|--------------------|----------------------------------------------------------------------------|-----------------------------------------------|
| `font-family`      | Defines the font type for the text.                                        | `font-family = "Verdana, sans-serif"`         |
| `font-size`        | Sets the font size.                                                       | `font-size = "1.5rem"`                        |
| `font-color`       | Defines the color of the text.                                             | `font-color = "#333"`                         |
| `background-color` | Sets a background color (useful for highlighter text).                    | `background-color = "#FFFF00"`                |
| `text-decoration`  | Applies underline, strikethrough, or none.                                | `text-decoration = "underline"`               |
| `alignment`        | Aligns text horizontally.                                                 | `alignment = "justify"`                       |
| `line-spacing`     | Adjusts the spacing between lines of text.                                | `line-spacing = "1.5"`                         |
| `letter-spacing`   | Adjusts the spacing between letters.                                       | `letter-spacing = "0.1em"`                    |
| `list-style-type`  | Defines the list marker style (circle, square, decimal).                  | `list-style-type = "circle"`                  |
| `hover.color`      | Changes the text color on hover.                                          | `hover.color = "#007BFF"`                     |
| `table.border`     | Defines the border style for a table.                                      | `table.border = "1px solid #333"`             |
| `table.header`     | Specifies styles for table headers.                                       | `table.header = { background-color = "#EEE" }` |
| `break.color`      | Defines the color of a break line.                                         | `break.color = "#333"`                        |
| `break.thickness`  | Defines the thickness of a break line.                                     | `break.thickness = "2px"`                     |
| `animations.enter` | Animation type for text entry (e.g., fade-in, typewriter).                | `animations.enter = "typewriter"`             |
| `animations.exit`  | Animation type for text exit (e.g., fade-out, slide).                     | `animations.exit = "fade-out"`                |
| `animations.duration` | Duration of the animation.                                              | `animations.duration = "1s"`                  |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "text"
style = "H1"
content = "Welcome to M3L!"
font = { family = "Verdana", size = "2rem" }
alignment = "center"
selectable = true
animations = { enter = "fade-in", exit = "fade-out", duration = "1s" }

[[layout.container.content]]
type = "text"
style = "paragraph"
content = "This is an example paragraph for demonstrating M3L text widgets."
font = { family = "Arial", size = "1rem" }
alignment = "justify"
line_spacing = "1.5"
letter_spacing = "0.05em"
selectable = true

[[layout.container.content]]
type = "text"
style = "link"
content = "Click here to learn more."
href = "@Undline/learn_more.m3l"
selectable = true

[[layout.container.content]]
type = "text"
style = "table"
table_data = [
    { row = ["Name", "Age"] },
    { row = ["Alice", "30"] },
    { row = ["Bob", "25"] }
]

[[layout.container.content]]
type = "text"
style = "break"
line_style = { color = "#333", thickness = "2px" }
```

---

### **Example GSS Implementation**
```toml
[text.header]
font-family = "Verdana, sans-serif"
font-size = "2rem"
font-color = "#333"
alignment = "center"
animations.enter = "fade-in"
animations.exit = "fade-out"
animations.duration = "1s"

[text.paragraph]
font-family = "Arial, sans-serif"
font-size = "1rem"
font-color = "#666"
line-spacing = "1.5"
letter-spacing = "0.05em"

[text.link]
font-family = "Arial, sans-serif"
font-size = "1rem"
font-color = "#007BFF"
text-decoration = "underline"

[text.link.hover]
font-color = "#0056b3"

[text.table]
font-family = "Arial, sans-serif"
font-size = "1rem"
font-color = "#333"
table.border = "1px solid #333"
table.header = { background-color = "#EEE" }

[text.break]
break.color = "#333"
break.thickness = "2px"
```

---

### **Additional Considerations**
- **UTF Support**: The M3L system fully supports UTF, enabling the use of multi-language text and non-ASCII characters.
- **Tooltips for Hyperlinks**: By default, tooltips display the hyperlink destination, enhancing user clarity.
- **Editable Text**: Not included by design; use a Text Area widget for editable content.
- **Animated Emojis**: Currently not implemented, but future extensions could enable animation for emoji or specific inline text elements.

---

### **Text Box**
- **Description**: A text box allows users to input single-line text. This widget supports rich interactivity and validation through events and intents.
- **Use Cases**:
  - Collecting user input (e.g., usernames, emails).
  - Password entry with secure visibility controls.
  - Real-time validation (e.g., regex, min/max length).
  - Dynamic interactions (e.g., triggering co-chain requests).

---

#### **Core Fields**
| Field           | Description                                                                 | Example                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `label`         | A descriptive title or prompt for the text box. Rendered via GSS styling.  | `label = "Enter Username"`                                                                                                                  |
| `placeholder`   | Text displayed inside the box when it is empty.                            | `placeholder = "Enter your username"`                                                                                                       |
| `default_value` | Pre-fills the text box with initial data.                                   | `default_value = "JohnDoe123"`                                                                                                |
| `password`      | Masks the input text for secure password entry.                            | `password = true`                                                                                                                             |
| `integrated_button` | Adds an interactive button inside the text box (e.g., toggle password visibility). | `integrated_button = { icon = "@Undline/assets/show_icon.svg", action = "toggle_visibility" }`                                            |
| `mask_symbol`   | Allows customization of the masking symbol for password fields.            | `mask_symbol = "•" or `mask_symbol = "🔒"`                                                                                                |
| `autocomplete`  | Suggests previously entered values as the user types.                      | `autocomplete = true`                                                                                                                         |
| `spellcheck`    | Enables or disables spellchecking for the input field.                     | `spellcheck = true`                                                                                                                           |
| `read_only`     | Prevents the user from modifying the text box value.                       | `read_only = true`                                                                                                                            |
| `max_length`    | Limits the number of characters a user can enter.                          | `max_length = 100`                                                                                                                            |
| `min_length`    | Specifies the minimum number of characters required.                       | `min_length = 5`                                                                                                                              |
| `case_transform`| Automatically transforms the input (e.g., uppercase, lowercase).           | `case_transform = "uppercase"`                                                                                                              |
| `on_input`      | Triggers actions as the user types.                                         | `on_input = [{ validate = "regex", pattern = "^[a-zA-Z0-9_]+$" }, { after_idle = "2s", intent = "check_availability", target = "UndChain://UnaS/namecheck" }]` |
| `on_exit`       | Triggers actions when the user leaves the text box.                        | `on_exit = [{ validate = "regex", pattern = "^[^@\s]+@[^@\s]+\.[^@\s]+$" }]`                                                        |
| `on_enter`      | Fires when the text box gains focus.                                        | `on_enter = [{ show_help = "Enter a unique username." }]`                                                                                   |
| `on_next`       | Handles navigation to the next widget in the flow.                         | `on_next = "password_field"`                                                                                                                |
| `on_submit`     | Fires when the user confirms input (e.g., pressing Enter).                 | `on_submit = [{ validate = "min_length", value = 3 }, { intent = "search", target = "SQeeL://Auction_House/search" }]`                  |
| `on_error`      | Triggers actions when an error specific to the widget occurs.              | `on_error = [{ display = "tooltip", message = "This field is required." }]`                                                               |

---

#### **Core Styling Parameters**
| Parameter           | Description                                             | Example                                        |
|---------------------|---------------------------------------------------------|------------------------------------------------|
| `font-family`       | Defines the font of the text inside the box.            | `font-family = "Arial, sans-serif"`          |
| `font-size`         | Sets the size of the text.                              | `font-size = "1rem"`                         |
| `color`             | Sets the text color.                                    | `color = "#333"`                              |
| `background-color`  | Defines the background color of the text box.           | `background-color = "#fff"`                  |
| `border`            | Specifies the border style, width, and color.           | `border = "1px solid #ccc"`                  |
| `border-radius`     | Rounds the corners of the text box.                     | `border-radius = "5px"`                      |
| `padding`           | Defines the padding inside the text box.                | `padding = "0.5rem"`                         |
| `placeholder.color` | Sets the color of the placeholder text.                 | `placeholder.color = "#aaa"`                 |
| `mask_symbol.style` | Defines the styling for the mask symbol in password fields. | `mask_symbol.style = "font-size: 1.2rem; color: #444;"`             |

---

#### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "text_box"
label = "Password"
placeholder = "Enter your password"
default_value = ""
password = true
mask_symbol = "🔒"
autocomplete = true
spellcheck = false
read_only = false
max_length = 20
case_transform = "uppercase"
integrated_button = { icon = "@Undline/assets/show_icon.svg", action = "toggle_visibility" }
on_input = [
    { validate = "min_length", value = 8, error_message = "Password must be at least 8 characters." },
    { validate = "regex", pattern = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", error_message = "Password must include letters and numbers." }
]
on_exit = [
    { validate = "regex", pattern = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", error_message = "Password must include letters and numbers." }
]
on_submit = [
    { intent = "submit_password", target = "UndChain://Account/Create" }
]
on_error = [
    { display = "tooltip", message = "Password does not meet requirements." }
]
```

---

#### **Example GSS Implementation**
```toml
[text_box]
font-family = "Arial, sans-serif"
border = "1px solid #ccc"
border-radius = "5px"
padding = "0.5rem"
color = "#333"
background-color = "#fff"

[text_box.label]
font-size = "1rem"
color = "#444"
padding-bottom = "0.25rem"

[text_box.placeholder]
color = "#aaa"
font-style = "italic"

[text_box.valid]
border-color = "#00FF00"

[text_box.invalid]
border-color = "#FF0000"

[text_box.waiting]
background-image = "loading_spinner.gif"

[text_box.integrated_button]
position = "absolute"
right = "1rem"
top = "50%"
transform = "translateY(-50%)"
width = "1.5rem"
height = "1.5rem"
cursor = "pointer"

[text_box.mask_symbol]
font-size = "1.2rem"
color = "#444"

[text_box.error.tooltip]
background-color = "#FFDDDD"
color = "#FF0000"
padding = "0.25rem"
border-radius = "3px"
```

---

### **Key Features**
- **Rich Event Handling**: Leverage `on_input`, `on_exit`, `on_enter`, `on_next`, `on_submit` and `on_error` for dynamic interactions and seamless user experiences.
- **Password Handling**: Use the `password` field for secure input, the `mask_symbol` for custom masking, and integrated buttons for toggling visibility.
- **Validation Options**: Support for client-side and co-chain validation ensures flexibility and scalability.
- **Dynamic Feedback**: Integrate GSS rules for valid, invalid, and waiting states to provide real-time feedback.
- **Accessibility**: Use ARIA roles and descriptions to enhance usability for assistive technologies.

---

### **Text Area**
- **Description**: A text area allows users to input multi-line text, making it ideal for feedback, comments, or larger bodies of text. This widget supports dynamic interactivity, validation, and user-friendly features like auto-expansion.
- **Use Cases**:
  - Collecting detailed user feedback or comments.
  - Enabling users to write multi-line notes or descriptions.
  - Integrating dynamic features like autosave or live character count.

---

#### **Core Fields**
| **Field**           | **Description**                                                                 | **Example**                                                                                                                         |
|---------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `label`             | A descriptive title or prompt for the text area. Rendered via GSS styling.      | `label = "Write Your Feedback"`                                                                                                   |
| `placeholder`       | Text displayed when the area is empty.                                          | `placeholder = "Enter your feedback here..."`                                                                                     |
| `default_value`     | Pre-fills the text area with initial data.                                       | `default_value = "I love M3L and GSS!"`                                                                                            |
| `max_length`        | Limits the total number of characters allowed.                                  | `max_length = 500`                                                                                                                 |
| `min_length`        | Specifies the minimum number of characters required.                           | `min_length = 10`                                                                                                                  |
| `min_lines`         | Sets the minimum number of lines the text area displays initially.             | `min_lines = 1`                                                                                                                    |
| `resizable`         | Allows users to resize the text area.                                           | `resizable = true`                                                                                                                 |
| `scrollable`        | Adds scrollbars if the content overflows.                                       | `scrollable = true`                                                                                                                |
| `collapsed`         | Specifies whether the text area starts collapsed.                              | `collapsed = true`                                                                                                                 |
| `collapsed_lines`   | Defines the number of lines shown when collapsed.                               | `collapsed_lines = 3`                                                                                                              |
| `max_lines`         | Sets the maximum number of lines the text area can grow to when expanded.      | `max_lines = 10`                                                                                                                   |
| `spellcheck`        | Enables or disables spellchecking.                                              | `spellcheck = true`                                                                                                                |
| `read_only`         | Prevents the user from modifying the content.                                   | `read_only = true`                                                                                                                 |
| `case_transform`    | Automatically transforms input to uppercase, lowercase, or capitalize each word.| `case_transform = "capitalize"`                                                                                                    |
| `character_count`   | Displays a live character count below the text area.                           | `character_count = true`                                                                                                           |
| `autosave`          | Automatically saves content after a set interval.                              | `autosave = { interval = "5s", target = "SQeeL://Notes/Save" }`                                                                  |
| `undo_redo`         | Enables undo and redo functionality for the text area.                         | `undo_redo = true`                                                                                                                 |
| `on_input`          | Triggers actions as the user types.                                             | `on_input = [{ validate = "regex", pattern = "^[a-zA-Z0-9\s]+$" }]`                                                              |
| `on_submit`         | Fires when the user confirms input (e.g., pressing Enter with `submit = true`). | `on_submit = [{ intent = "submit_comment", target = "SQeeL://Comments/Submit" }]`                                                  |
| `on_error`          | Triggers actions when an error specific to the widget occurs.                  | `on_error = [{ display = "tooltip", message = "Comment must be at least 10 characters." }]`                                        |
| `onscreen_keyboard` | Activates an on-screen keyboard when the text area gains focus.                | `onscreen_keyboard = true`                                                                                                          |
| `on_enter`          | Triggers actions when the text area gains focus.                              | `on_enter = [{ highlight_border = true }]`                                                                                          |
| `on_exit`           | Fires actions when the text area loses focus.                                 | `on_exit = [{ autosave = true }]`                                                                                                   |
| `on_highlight`      | Detects when text within the area is highlighted and triggers an action.       | `on_highlight = [{ show_menu = "mini-menu" }]`                                                                                     |
| `on_next`           | Handles navigation to the next widget in the flow (e.g., via Tab key).         | `on_next = "next_widget_id"`                                                                                                       |

---

#### **Core Styling Parameters**
| **Parameter**          | **Description**                                              | **Example**                                    |
|------------------------|-------------------------------------------------------------|-----------------------------------------------|
| `font-family`          | Defines the font of the text inside the area.               | `font-family = "Verdana, sans-serif"`        |
| `font-size`            | Sets the size of the text.                                  | `font-size = "1rem"`                         |
| `font-color`           | Sets the font color of the text inside the area.            | `font-color = "#333"`                        |
| `background-color`     | Sets the background color of the area.                      | `background-color = "#fff"`                  |
| `border`               | Specifies the border style, width, and color.               | `border = "1px solid #ddd"`                  |
| `border-radius`        | Rounds the corners of the text area.                        | `border-radius = "8px"`                      |
| `padding`              | Sets the padding inside the area.                           | `padding = "1rem"`                           |
| `placeholder.color`    | Sets the color of the placeholder text.                     | `placeholder.color = "#aaa"`                 |
| `scrollbar.color`      | Sets the color of the scrollbar for scrollable areas.       | `scrollbar.color = "#ccc"`                   |
| `resize.handle.style`  | Styles the resize handle when `resizable = true`.           | `resize.handle.style = "width: 8px; color: #444;"` |
| `collapsed.height`     | Sets the height of the collapsed text area.                 | `collapsed.height = "3rem"`                  |
| `expanded.height`      | Sets the height of the expanded text area.                  | `expanded.height = "10rem"`                  |
| `character_count.style`| Styles the character count displayed below the text area.   | `character_count.style = "font-size: 0.9rem; color: #666;"` |
| `touch.focus_indicator`| Sets styling for when the text area is focused on touch devices. | `touch.focus_indicator = "border: 2px solid #007BFF;"` |

---

#### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "text_area"
label = "Write Your Feedback"
placeholder = "Enter your feedback here..."
default_value = ""
max_length = 500
min_length = 10
min_lines = 1
resizable = true
scrollable = true
collapsed = true
collapsed_lines = 3
max_lines = 10
spellcheck = true
character_count = true
autosave = { interval = "5s", target = "SQeeL://Feedback/Save" }
onscreen_keyboard = true
on_input = [
    { validate = "min_length", value = 10, error_message = "Feedback must be at least 10 characters." },
    { validate = "regex", pattern = "^[a-zA-Z0-9\s.,!?]+$", error_message = "Only alphanumeric characters, spaces, and punctuation are allowed." }
]
on_enter = [
    { highlight_border = true }
]
on_exit = [
    { autosave = true }
]
on_highlight = [
    { show_menu = "mini-menu" }
]
on_next = "next_widget_id"
on_submit = [
    { intent = "submit_feedback", target = "SQeeL://Feedback/Submit" }
]
on_error = [
    { display = "tooltip", message = "Feedback submission failed. Try again." }
]
```

---

#### **Example GSS Implementation**
```toml
[text_area]
font-family = "Verdana, sans-serif"
border = "1px solid #ddd"
border-radius = "8px"
padding = "1rem"
font-color = "#333"
background-color = "#fff"

[text_area.label]
font-size = "1rem"
color = "#444"
padding-bottom = "0.5rem"

[text_area.placeholder]
color = "#aaa"
font-style = "italic"

[text_area.character_count]
font-size = "0.9rem"
color = "#666"
margin-top = "0.25rem"

[text_area.valid]
border-color = "#00FF00"

[text_area.invalid]
border-color = "#FF0000"

[text_area.scrollbar]
color = "#ccc"

[text_area.resize.handle]
width = "8px"
color = "#444"

[text_area.collapsed]
height = "3rem"

[text_area.expanded]
height = "10rem"

[text_area.touch.focus_indicator]
border = "2px solid #007BFF"
background-color = "#f0f8ff"
```

---

### **Key Features**
- **Rich Event Handling**: Leverage `on_input`, `on_submit`, `on_error`, `on_enter`, `on_exit`, `on_highlight`, and `on_next` for dynamic interactions and seamless user experiences.
- **Collapsible Design**: Use the `collapsed` parameter to save space while still allowing expandable text entry.
- **Dynamic Feedback**: Integrate GSS rules for valid, invalid, and waiting states to provide real-time feedback.
- **Autosave and Undo/Redo**: Automatically save progress and allow users to undo/redo changes for better usability.
- **Accessibility**: Use ARIA roles and descriptions to enhance usability for assistive technologies.
- **Touch Optimization**: Parameters like `onscreen_keyboard` ensure smooth interaction on touch devices.

---

#### **Notes**
- **Width Behavior**: The width of the text area is defined by the total width of the widget's containing element.
- **Height Behavior**: If `min_lines` and `max_lines` are not defined, the height of the text area defaults to the height of the containing widget.

---

### **Checkbox Widget**

Checkboxes are versatile widgets for binary or ternary selections (checked, unchecked, and indeterminate). They support custom styling, animations, and advanced interactions for hierarchical structures (parent-child relationships).

---

### **Core Features**
1. **Customizable Check Style**:
   - GSS developers can define the appearance of the checkmark (e.g., ✔, X, custom icons, or even animations).
   - Option to use images or SVGs for the checkmark.

2. **State Management**:
   - **Checked**: Indicates the checkbox is selected.
   - **Unchecked**: Indicates the checkbox is unselected.
   - **Indeterminate**: Used for parent-child relationships when only some child checkboxes are selected.

3. **Keyboard Navigation**:
   - By default, the `spacebar` toggles the checkbox state, but GSS developers can override this behavior.

4. **Interactive Events**:
   - Supports events like `on_click`, `on_hover`, and `on_change`.

5. **Accessibility**:
   - Labels for screen readers (e.g., `aria-label` equivalent).
   - Fully operable with keyboard input.

---

### **Proposed Fields**
| **Field**       | **Description**                                                             | **Example**                              |
|-----------------|-----------------------------------------------------------------------------|------------------------------------------|
| `label`         | Text displayed next to the checkbox.                                        | `label = "Subscribe to newsletter"`      |
| `state`         | Current state of the checkbox (`checked`, `unchecked`, `indeterminate`).    | `state = "checked"`                      |
| `group`         | Groups multiple checkboxes for logical association.                        | `group = "preferences"`                  |
| `animations`    | Animations for state transitions (check/uncheck).                          | `animations = { check = "bounce", uncheck = "fade-out" }` |
| `tooltip`       | Tooltip displayed on hover.                                                | `tooltip = "Click to subscribe"`         |
| `disabled`      | Disables the checkbox, preventing interaction.                             | `disabled = true`                        |

---

### **GSS Styling Parameters**
| **Parameter**        | **Description**                                                      | **Example**                              |
|----------------------|----------------------------------------------------------------------|------------------------------------------|
| `font-family`        | Defines the font for the checkbox label.                            | `font-family = "Arial, sans-serif"`      |
| `font-size`          | Defines the size of the label text.                                 | `font-size = "1rem"`                     |
| `font-color`         | Color of the label text.                                            | `font-color = "#333"`                    |
| `checkmark`          | Defines the style of the checkmark (e.g., ✔, X, image).             | `checkmark = "✔"`                        |
| `checkmark.color`    | Color of the checkmark.                                             | `checkmark.color = "#007BFF"`            |
| `checkmark.size`     | Size of the checkmark relative to the box.                          | `checkmark.size = "80%"`                 |
| `box.size`           | Size of the checkbox itself.                                        | `box.size = "20px"`                      |
| `box.border`         | Border style of the checkbox.                                       | `box.border = "1px solid #333"`          |
| `box.background`     | Background color of the checkbox when unchecked.                   | `box.background = "#FFF"`                |
| `box.hover.background` | Background color of the checkbox on hover.                        | `box.hover.background = "#EEE"`          |
| `box.indeterminate`  | Styling for the indeterminate state (e.g., dash or icon).           | `box.indeterminate = "-"`                |
| `animations.check`   | Animation applied when the checkbox is checked.                    | `animations.check = "bounce"`            |
| `animations.uncheck` | Animation applied when the checkbox is unchecked.                  | `animations.uncheck = "fade-out"`        |

---

### **Example M3L Implementation**
#### **Parent-Child Group Example**
```toml
[[layout.container.content]]
id = "parent-checkbox"
type = "checkbox"
label = "All notifications"
state = "indeterminate"
children = [
    {
        id = "child-email",
        type = "checkbox",
        label = "Email notifications",
        state = "checked"
    },
    {
        id = "child-push",
        type = "checkbox",
        label = "Push notifications",
        state = "unchecked"
    }
]
```

---

### **Example GSS Implementation**
```toml
[checkbox]
font-family = "Arial, sans-serif"
font-size = "1rem"
font-color = "#333"
box.size = "20px"
box.border = "1px solid #333"
box.background = "#FFF"
box.hover.background = "#EEE"

[checkbox.checkmark]
content = "✔"
color = "#007BFF"
size = "80%"

[checkbox.indeterminate]
content = "-"
color = "#FFA500"

[checkbox.animations]
check = "bounce"
uncheck = "fade-out"
```

---

### **Advanced Considerations**
1. **Parent-Child Relationships**:
   - Parent checkboxes automatically toggle all child checkboxes.
   - Indeterminate state updates dynamically based on child selections.

2. **Keyboard Navigation**:
   - By default, `spacebar` toggles the checkbox state. GSS developers can redefine this behavior for custom accessibility setups.

3. **Future Node Animation Placeholder**:
   - Parallel animations could enable dynamic effects (e.g., glow and bounce simultaneously).
   - **Example Hypothetical**:
     ```toml
     [checkbox.animations.parallel]
     nodes = [
         { type = "glow", color = "#007BFF", duration = "0.3s" },
         { type = "bounce", duration = "0.5s" }
     ]
     ```

---

### **Conclusion**
Checkboxes provide a flexible solution for binary and ternary selection scenarios. By supporting advanced features like animations, parent-child relationships, and customizable styling, they can adapt to various application needs. Future enhancements, such as node-based animations, promise even greater creative possibilities for GSS developers.

---

### **Radio Button Widget**

Radio buttons are versatile widgets that allow users to select a single option from multiple choices within a group. They share many similarities with checkboxes but are mutually exclusive within their group.

---

### **Core Features**
1. **Single Selection Per Group**:
   - Radio buttons within the same group allow only one selection at a time.

2. **Customizable Selection Style**:
   - GSS developers can define the appearance of the selection indicator (e.g., filled circle, checkmark, custom SVG).

3. **Keyboard Navigation**:
   - By default, `arrow keys` navigate between options, and `spacebar` selects an option.

4. **State Management**:
   - Tracks the currently selected option within a group.

5. **Interactive Events**:
   - Supports events like `on_click`, `on_hover`, `on_change`, `on_enter`, and `on_exit`.

6. **Accessibility**:
   - Labels for screen readers (e.g., `aria-label` equivalent).
   - Fully operable with keyboard input.

---

### **Proposed Fields**
| **Field**       | **Description**                                                | **Example**                              |
|-----------------|----------------------------------------------------------------|------------------------------------------|
| `label`         | Text displayed next to the radio button.                       | `label = "Option 1"`                     |
| `state`         | Current state of the radio button (`selected`, `unselected`).  | `state = "selected"`                     |
| `group`         | Defines the group the radio button belongs to.                | `group = "choices"`                      |
| `tooltip`       | Tooltip displayed on hover.                                   | `tooltip = "Select this option"`         |
| `disabled`      | Disables the radio button, preventing interaction.            | `disabled = true`                        |
| `animations`    | Animations for state transitions (select/unselect).           | `animations = { select = "pulse", unselect = "fade-out" }` |

---

### **GSS Styling Parameters**
| **Parameter**          | **Description**                                                    | **Example**                              |
|------------------------|--------------------------------------------------------------------|------------------------------------------|
| `font-family`          | Defines the font for the radio button label.                      | `font-family = "Arial, sans-serif"`      |
| `font-size`            | Defines the size of the label text.                               | `font-size = "1rem"`                     |
| `font-color`           | Color of the label text.                                          | `font-color = "#333"`                    |
| `indicator`            | Defines the style of the selection indicator.                    | `indicator = "circle"`                   |
| `indicator.color`      | Color of the selection indicator.                                | `indicator.color = "#007BFF"`            |
| `indicator.size`       | Size of the indicator relative to the radio button.              | `indicator.size = "80%"`                 |
| `indicator.svg`        | Path to a custom SVG for the selection indicator.                | `indicator.svg = "@assets/selector.svg"` |
| `box.size`             | Size of the radio button itself.                                 | `box.size = "20px"`                      |
| `box.border`           | Border style of the radio button.                                | `box.border = "1px solid #333"`          |
| `box.background`       | Background color of the radio button when unselected.            | `box.background = "#FFF"`                |
| `box.hover.background` | Background color of the radio button on hover.                   | `box.hover.background = "#EEE"`          |
| `animations.select`    | Animation applied when the radio button is selected.             | `animations.select = "pulse"`            |
| `animations.unselect`  | Animation applied when the radio button is unselected.           | `animations.unselect = "fade-out"`       |
| `animations.enter`     | Animation triggered when the radio button gains focus.           | `animations.enter = "glow"`              |
| `animations.exit`      | Animation triggered when the radio button loses focus.           | `animations.exit = "fade-out"`           |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "radio_button"
group = "choices"
children = [
    {
        label = "Option 1",
        state = "selected",
        tooltip = "Select Option 1",
        animations = { select = "pulse", unselect = "fade-out", enter = "glow", exit = "fade-out" }
    },
    {
        label = "Option 2",
        state = "unselected",
        tooltip = "Select Option 2",
        animations = { select = "pulse", unselect = "fade-out", enter = "glow", exit = "fade-out" }
    },
    {
        label = "Option 3",
        state = "unselected",
        tooltip = "Select Option 3",
        animations = { select = "pulse", unselect = "fade-out", enter = "glow", exit = "fade-out" }
    }
]
```

---

### **Example GSS Implementation**
```toml
[radio_button]
font-family = "Arial, sans-serif"
font-size = "1rem"
font-color = "#333"
box.size = "20px"
box.border = "1px solid #333"
box.background = "#FFF"
box.hover.background = "#EEE"

[radio_button.indicator]
style = "circle"
color = "#007BFF"
size = "80%"
svg = "@assets/selector.svg"

[radio_button.animations]
select = "pulse"
unselect = "fade-out"
enter = "glow"
exit = "fade-out"
```

---

### **Conclusion**
Radio buttons provide an intuitive solution for single-selection scenarios. With features like animations, custom indicators, and advanced accessibility options, they offer a highly customizable and interactive user experience.

---

### **Navigation Box Widget**

The Navigation Box Widget provides an intuitive and customizable interface for displaying breadcrumbs, helping users navigate hierarchical structures such as file systems, web directories, or dynamic folder paths.

---

### **Core Features**

1. **Breadcrumb Display**:

   - Dynamically generate breadcrumbs based on the current navigation path.
   - Each breadcrumb is customizable to be interactive, static, or styled for visual emphasis.

2. **Custom Separator Support**:

   - Allows designers to specify custom separators (e.g., `/`, `>`, `|`, icons, or SVGs).
   - Default separator: `/`.

3. **Truncation and Overflow Handling**:

   - Automatically truncates paths that exceed the character limit of the navigation bar.
   - Supports scrolling or a special "more" SVG/icon to indicate hidden paths.
   - Optional animation for truncation (e.g., sliding folders into the "more" area).

4. **Dynamic Data Integration**:

   - Supports fuzzy finding for user input when typing a path.
   - Dynamically updates breadcrumbs based on changes to the navigation path. Useful in cases where a folder or directory has many folders and users are manually typing out a path.

5. **Interactive Events**:

   - Supports events like `on_click`, `on_hover`, `on_focus`, `on_enter`, and `on_exit`.
   - Flexible enough to accommodate keyboard, mouse, touch, and controller inputs.

6. **Accessibility**:

   - Provides screen reader-friendly labels for breadcrumbs and separators.
   - Fully supports keyboard and controller navigation.

---

### **Proposed Fields**

| **Field**     | **Description**                                             | **Example**                                                                          |
| ------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `path`        | The current navigation path as an array of nodes.           | `path = ["@username", "Documents", "Projects"]`                                      |
| `separator`   | The character, icon, or SVG separating breadcrumbs.         | `separator = ">"`                                                                    |
| `interactive` | Determines if breadcrumbs are clickable or static.          | `interactive = true`                                                                 |
| `tooltip`     | Tooltip for each breadcrumb, showing additional context.    | `tooltip = "Click to return to Home"`                                                |
| `animations`  | Animations for adding, removing, or truncating breadcrumbs. | `animations = { enter = "slide-right", exit = "fade-out", truncate = "slide-left" }` |

---

### **GSS Styling Parameters**

| **Parameter**         | **Description**                                              | **Example**                                 |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------- |
| `font-family`         | Defines the font for breadcrumb text.                        | `font-family = "Arial, sans-serif"`         |
| `font-size`           | Defines the size of breadcrumb text.                         | `font-size = "1rem"`                        |
| `font-color`          | Color of breadcrumb text.                                    | `font-color = "#333"`                       |
| `hover.color`         | Color of breadcrumb text on hover.                           | `hover.color = "#007BFF"`                   |
| `separator.style`     | Style of the separator symbol (e.g., font, color, SVG path). | `separator.style = { font-color = "#999" }` |
| `animations.enter`    | Animation applied when a breadcrumb is added.                | `animations.enter = "slide-right"`          |
| `animations.exit`     | Animation applied when a breadcrumb is removed.              | `animations.exit = "fade-out"`              |
| `animations.truncate` | Animation applied when truncating breadcrumbs.               | `animations.truncate = "slide-left"`        |
| `overflow.icon`       | Icon or SVG used to indicate truncated paths.                | `overflow.icon = "@assets/more.svg"`        |

---

### **Example M3L Implementation**

```toml
[[layout.container.content]]
type = "navigation_box"
path = ["Home", "Documents", "Projects"]
separator = "/"
interactive = true
animations = { enter = "slide-right", exit = "fade-out", truncate = "slide-left" }
```

---

### **Example GSS Implementation**

```toml
[navigation_box]
font-family = "Arial, sans-serif"
font-size = "1rem"
font-color = "#333"

[navigation_box.separator]
style = "/"
font-color = "#999"

[navigation_box.animations]
enter = "slide-right"
exit = "fade-out"
truncate = "slide-left"

[navigation_box.hover]
font-color = "#007BFF"

[navigation_box.overflow]
icon = "@assets/more.svg"
```

---

### **Advanced Considerations**

1. **Input Adaptability**:

   - GSS developers can redefine how users interact with breadcrumbs (e.g., clicking, hovering, or using keyboard/controller shortcuts).

2. **Dynamic Path Updates**:

   - Integration with co-chains (e.g., Pages) to fetch and update navigation paths dynamically.

3. **Fuzzy Finding**:

   - Enable users to type a path manually and suggest completions based on available folders.

4. **Truncation Enhancements**:

   - Allow users to interact with truncated paths by clicking the "more" icon to expand hidden breadcrumbs.

5. **Custom Separators**:

   - Support for SVGs or complex icons as separators for highly customized designs.

---

### **Conclusion**

The Navigation Box Widget provides an essential tool for hierarchical navigation. With support for advanced animations, custom separators, and dynamic updates, it adapts seamlessly to both static and dynamic navigation scenarios. The flexibility of GSS ensures a consistent yet customizable user experience across devices and input types.

---

### **Scroll Area Widget**

The Scroll Area Widget provides an intuitive way to navigate additional content within a limited space. It supports vertical, horizontal, or bidirectional scrolling and offers extensive customization options for behavior, appearance, and interactivity.

---

### **Core Features**
1. **Orientation**:
   - Supports vertical, horizontal, or both directions for scrolling.

2. **Customizable Scrollbars**:
   - Options for scrollbar visibility (always visible, auto-hide after inactivity, or hidden).
   - Styleable scrollbar appearance, including size, color, gradients, patterns, and even images with repeating patterns.
   - Supports active scrollbars that change visually based on scroll progress (e.g., gradients).

3. **Easing and Smooth Scrolling**:
   - Allows GSS designers to define easing effects for a custom scrolling feel.
   - Supports different easing curves (e.g., linear, ease-in, ease-out).

4. **Interactive Events**:
   - Events like `on_scroll`, `on_scroll_end`, `on_scroll_start`, `on_reach_end`, `on_enter`, and `on_exit`.
   - Example: `on_enter` could trigger a subtle wiggle animation to hint at scrollability.

5. **Infinite Scroll Support**:
   - Dynamically loads additional content as users scroll, with visual indicators for infinite scrolling.

6. **Responsive Design**:
   - Automatically adjusts to the available view area, ensuring compatibility across devices and orientations.

7. **Accessibility**:
   - Provides clear indicators for scrollable areas and supports keyboard and controller navigation.

---

### **Proposed Fields**
| **Field**          | **Description**                                                        | **Example**                            |
|--------------------|------------------------------------------------------------------------|----------------------------------------|
| `orientation`      | Defines the scroll direction (`vertical`, `horizontal`, or `both`).    | `orientation = "vertical"`             |
| `scrollbar`        | Configures scrollbar behavior (`visible`, `hidden`, or `auto-hide`).   | `scrollbar = "auto-hide"`              |
| `easing`           | Defines the easing effect for scrolling.                              | `easing = "ease-in-out"`               |
| `scroll_speed`     | Adjusts the speed of the scroll.                                       | `scroll_speed = "normal"`              |
| `infinite_scroll`  | Enables infinite scrolling, dynamically loading more content.          | `infinite_scroll = true`               |
| `padding`          | Padding around the scrollable content.                                | `padding = "10px"`                     |
| `margin`           | Margin around the scroll area container.                              | `margin = "15px"`                      |

---

### **GSS Styling Parameters**
| **Parameter**          | **Description**                                                    | **Example**                            |
|------------------------|--------------------------------------------------------------------|----------------------------------------|
| `scrollbar.size`       | Size (thickness) of the scrollbar.                                | `scrollbar.size = "8px"`               |
| `scrollbar.color`      | Color of the scrollbar.                                           | `scrollbar.color = "#333"`             |
| `scrollbar.track.color`| Color of the scrollbar track.                                     | `scrollbar.track.color = "#EEE"`       |
| `scrollbar.pattern`    | Image or pattern used for the scrollbar.                         | `scrollbar.pattern = "@assets/bar.png"`|
| `scrollbar.gradient`   | Gradient for the scrollbar that changes with scroll position.     | `scrollbar.gradient = "linear-gradient(to bottom, #007BFF, #FFF)"` |
| `easing`               | Defines the easing curve for scrolling behavior.                 | `easing = "ease-in-out"`               |
| `scrollbar.auto-hide`  | Duration before the scrollbar auto-hides (if enabled).            | `scrollbar.auto-hide = "2s"`           |
| `animations.enter`     | Animation applied when the scroll area is entered.                | `animations.enter = "wiggle"`          |
| `animations.exit`      | Animation applied when the scroll area is exited.                 | `animations.exit = "fade-out"`         |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "scroll_area"
orientation = "vertical"
scrollbar = "auto-hide"
easing = "ease-in-out"
scroll_speed = "normal"
infinite_scroll = true
padding = "10px"
margin = "15px"

children = [
    {
        type = "text",
        content = "This is some scrollable content.",
        style = "paragraph"
    },
    {
        type = "text",
        content = "Keep scrolling to see more.",
        style = "paragraph"
    }
]
```

---

### **Example GSS Implementation**
```toml
[scroll_area]
padding = "10px"
margin = "15px"

[scroll_area.scrollbar]
size = "8px"
color = "#333"
track.color = "#EEE"
pattern = "@assets/bar.png"
gradient = "linear-gradient(to bottom, #007BFF, #FFF)"
auto-hide = "2s"

[scroll_area.easing]
easing = "ease-in-out"

[scroll_area.animations]
enter = "wiggle"
exit = "fade-out"
```

---

### **Advanced Considerations**
1. **Infinite Scroll Enhancements**:
   - Allow visual indicators (e.g., "Loading..." or spinners) during content fetch.
   - GSS designers can customize styles for loading indicators.

2. **Custom Scrollbar Design**:
   - Include support for SVGs, animations, and dynamic patterns for the scrollbar.

3. **Truncation Enhancements**:
   - Automatically adjust the scroll area’s dimensions based on the parent container.

4. **Event Handling**:
   - Add support for events like:
     - `on_scroll_start`: Triggered when scrolling begins.
     - `on_scroll_end`: Triggered when scrolling stops.
     - `on_reach_end`: Triggered when the user scrolls to the end of the content.

5. **Cross-Device Compatibility**:
   - Ensure smooth and intuitive scrolling behavior across mouse, touch, and controller inputs.

---

### **Conclusion**
The Scroll Area Widget provides a versatile and visually appealing solution for handling overflow content. With advanced features like infinite scrolling, custom scrollbar designs, and dynamic interactions, it adapts seamlessly to diverse application needs and enhances the user experience across all input types.

---

### **Drop Menu Widget**

The Drop Menu Widget provides a versatile way to present a collapsible list of options for selection. It supports single or multi-option selection, dynamic content, advanced interactivity, and now includes both visual and audio animation support for enhanced engagement.

---

### **Core Features**
1. **Single or Multi-Select**:
   - Supports single-option or multi-option selection.
   - Multi-select menus can include checkboxes or toggles for selection.

2. **Grouped Options**:
   - Allows grouping of related options under headers.
   - Supports dividers for logical separation of option groups.

3. **Customizable Behavior**:
   - Define whether the menu opens on hover, click, or another interaction.
   - Optionally allow the menu to remain open after a selection.

4. **Dynamic Content**:
   - Fetch options dynamically from co-chains or APIs.
   - Auto-update when the data source changes.
   - Example: Place the co-chain link in the `options` field to fetch options dynamically.

5. **Searchable Menus**:
   - Auto-completes or jumps to options as the user begins typing.

6. **Images and Colors for Options**:
   - Allows options to include images or icons next to text.
   - Supports color-coded options or groups for better visual distinction.

7. **Animations (Visual and Audio)**:
   - Smooth animations for menu opening, closing, item highlighting, and selection.
   - Audio can be defined as a "parallel animation" within the animation configuration.

8. **Interactive Events**:
   - Events like `on_open`, `on_close`, `on_item_hover`, and `on_item_select` for granular interactivity.

9. **Accessibility**:
   - Keyboard and controller navigable.
   - Screen reader-friendly labels for each option.

10. **Overflow Handling**:
    - Automatically scrolls or truncates long option lists.

---

### **Proposed Fields**
| **Field**          | **Description**                                                        | **Example**                              |
|--------------------|------------------------------------------------------------------------|------------------------------------------|
| `options`          | An array of options or a link to a data source.                       | `options = ["Option 1", "Option 2"]`     |
| `multi_select`     | Enables multi-option selection.                                       | `multi_select = false`                   |
| `default`          | The default selected option(s).                                       | `default = "Option 1"`                   |
| `placeholder`      | Text displayed when no option is selected.                            | `placeholder = "Select an option"`       |
| `grouped_options`  | Logical grouping of options with headers or dividers.                 | `grouped_options = true`                 |
| `open_behavior`    | Defines the behavior for opening the menu (`hover`, `click`).         | `open_behavior = "click"`                |
| `animations`       | Animations for opening, closing, and highlighting, including audio.   | `animations = { open = { type = "fade-in", audio = "open.wav" }, close = { type = "fade-out", audio = "close.wav" }, on_item_hover = { type = "scale-up", audio = "hover.wav" }, on_item_select = { type = "pulse", audio = "select.wav" } }` |
| `searchable`       | Enables a search feature for large option sets.                      | `searchable = true`                      |
| `max_height`       | Maximum height for the dropdown menu before enabling scrolling.       | `max_height = "200px"`                   |
| `option_images`    | Includes images or icons next to text in options.                    | `option_images = true`                   |
| `option_colors`    | Assigns colors to specific options or groups.                        | `option_colors = true`                   |

---

### **GSS Styling Parameters**
| **Parameter**          | **Description**                                                    | **Example**                              |
|------------------------|--------------------------------------------------------------------|------------------------------------------|
| `menu.font-family`     | Defines the font for menu text.                                   | `menu.font-family = "Arial, sans-serif"` |
| `menu.font-size`       | Defines the size of menu text.                                    | `menu.font-size = "1rem"`                |
| `menu.background`      | Background color of the dropdown menu.                           | `menu.background = "#FFF"`               |
| `menu.border`          | Border style of the dropdown menu.                               | `menu.border = "1px solid #333"`         |
| `menu.hover.background`| Background color of menu items on hover.                         | `menu.hover.background = "#EEE"`         |
| `menu.selected.color`  | Color of selected menu items.                                     | `menu.selected.color = "#007BFF"`        |
| `menu.option.image`    | Styling for images/icons next to options.                        | `menu.option.image = { size = "16px" }`  |
| `menu.option.color`    | Styling for color-coded options.                                 | `menu.option.color = "#FF5733"`          |
| `group.header.style`   | Styling for grouped option headers.                              | `group.header.style = { font-weight = "bold" }` |
| `group.divider.style`  | Styling for dividers between option groups.                      | `group.divider.style = { color = "#CCC" }` |
| `animations.open`      | Animation applied when the menu opens.                           | `animations.open = { type = "fade-in", audio = "open.wav" }` |
| `animations.close`     | Animation applied when the menu closes.                          | `animations.close = { type = "fade-out", audio = "close.wav" }` |
| `animations.on_item_hover` | Animation applied when an item is hovered over.              | `animations.on_item_hover = { type = "scale-up", audio = "hover.wav" }` |
| `animations.on_item_select`| Animation applied when an item is selected.                  | `animations.on_item_select = { type = "pulse", audio = "select.wav" }` |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "drop_menu"
placeholder = "Select an option"
multi_select = true
default = ["Option 1"]
open_behavior = "click"
searchable = true
options = [
    { group = "Favorites", options = [
        { text = "Option 1", image = "@assets/icon1.png", color = "#FF5733" },
        { text = "Option 2", image = "@assets/icon2.png", color = "#33FF57" }
    ] },
    { group = "More Options", options = [
        { text = "Option 3", image = "@assets/icon3.png", color = "#3357FF" },
        { text = "Option 4", image = "@assets/icon4.png", color = "#5733FF" }
    ] }
]
animations = { open = { type = "fade-in", audio = "open.wav" }, close = { type = "fade-out", audio = "close.wav" }, on_item_hover = { type = "scale-up", audio = "hover.wav" }, on_item_select = { type = "pulse", audio = "select.wav" } }
```

---

### **Example GSS Implementation**
```toml
[drop_menu]
font-family = "Arial, sans-serif"
font-size = "1rem"
background = "#FFF"
border = "1px solid #333"

[drop_menu.menu.hover]
background = "#EEE"

[drop_menu.menu.selected]
color = "#007BFF"

[menu.option.image]
size = "16px"

[menu.option.color]
default = "#FF5733"
hover = "#007BFF"

[group.header]
style = { font-weight = "bold", font-size = "1.2rem" }

[group.divider]
style = { color = "#CCC", thickness = "1px" }

[drop_menu.animations]
open = { type = "fade-in", audio = "open.wav" }
close = { type = "fade-out", audio = "close.wav" }
on_item_hover = { type = "scale-up", audio = "hover.wav" }
on_item_select = { type = "pulse", audio = "select.wav" }
```

---

### **Advanced Considerations**
1. **Searchable Menus**:
   - Auto-completes or jumps to options as the user begins typing.

2. **Grouped Options**:
   - Logical separation for improved user clarity.
   - Dividers and headers to visually distinguish sections.

3. **Dynamic Content**:
   - Fetch menu options dynamically from co-chains or APIs.
   - Place the link in the `options` field to enable dynamic fetching.

4. **Custom Option Styling**:
   - Allow GSS developers to style individual options uniquely.
   - Include options for images/icons and color-coding.

5. **Multi-Device Compatibility**:
   - Ensure intuitive behavior across mouse, touch, and controller inputs.

6. **Audio Feedback as Parallel Animation**:
   - Integrate audio cues within the animation configuration for streamlined implementation and synchronized effects.

---

### **Conclusion**
The Drop Menu Widget offers a highly flexible and interactive solution for presenting selectable options. With features like grouping, animations, dynamic data, search capabilities, and visual/audio enhancements, it adapts seamlessly to various use cases while ensuring an engaging user experience across all devices and input methods.

---

### **Item Grid Widget**

The Item Grid Widget organizes items or elements into a grid layout, allowing users to interact with each cell. It is ideal for inventory systems, file management, or visual data organization and is designed to be intuitive across multiple input devices, including controllers.

---

### **Core Features**
1. **Grid Layout**:
   - Configurable rows and columns.
   - Dynamically adjusts based on available space or item count.

2. **Navigation**:
   - Fully navigable with keyboard, touch, and controller inputs.
   - Supports `on_focus`, `on_select`, and `on_hover` events for each grid cell.

3. **Cell Customization**:
   - Cells can contain images, icons, text, or interactive widgets (e.g., buttons or toggles).
   - Background colors for each cell to indicate specific asset types.

4. **Dynamic Updates**:
   - Add, remove, or rearrange items dynamically.
   - Option to load content from co-chains.
   - Includes loading animations to indicate asset retrieval.

5. **Grouping**:
   - Support for grouping items within bordered sections (e.g., digital asset categories).
   - Borders can be styled or colored for visual clarity.

6. **Accessibility**:
   - Provides labels or tooltips for each cell.
   - Supports focus management for screen readers.

7. **Animations**:
   - Smooth animations for item addition, removal, rearrangement, and loading.
   - Optional visual effects on selection or focus.

---

### **Proposed Fields**
| **Field**        | **Description**                                                     | **Example**                              |
|------------------|---------------------------------------------------------------------|------------------------------------------|
| `grid_size`      | Defines the number of rows and columns.                             | `grid_size = { rows = 4, columns = 5 }`  |
| `cell_size`      | Dimensions of each grid cell.                                       | `cell_size = "64px"`                   |
| `items`          | Array of items to display in the grid.                              | `items = ["sword.png", "shield.png"]` |
| `dynamic`        | Enables dynamic item management (e.g., add/remove items).           | `dynamic = true`                         |
| `loading_animation` | Animation shown while assets are loading.                        | `loading_animation = "spin"`           |
| `grouping`       | Defines groups of items with visual borders.                        | `grouping = true`                        |
| `navigation`     | Configures navigation behavior for controllers and keyboards.       | `navigation = "controller"`            |
| `animations`     | Animations for item interactions.                                   | `animations = { add = "fade-in", remove = "fade-out" }` |

---

### **GSS Styling Parameters**
| **Parameter**         | **Description**                                                | **Example**                              |
|-----------------------|----------------------------------------------------------------|------------------------------------------|
| `grid.gap`            | Spacing between grid cells.                                    | `grid.gap = "10px"`                    |
| `grid.background`     | Background color of the grid.                                  | `grid.background = "#333"`             |
| `cell.border`         | Border style for each cell.                                    | `cell.border = "1px solid #FFF"`       |
| `cell.hover.effect`   | Visual effect on hover.                                        | `cell.hover.effect = "glow"`           |
| `cell.selected.effect`| Effect for selected cells.                                     | `cell.selected.effect = "scale-up"`    |
| `cell.loading.animation` | Animation for loading items into a cell.                   | `cell.loading.animation = "spin"`      |
| `cell.background.color` | Background color for individual cells (e.g., asset type).    | `cell.background.color = "#FF5733"`    |
| `group.border`        | Border style for item groups.                                  | `group.border = "2px solid #CCC"`      |
| `group.background`    | Background color for grouped areas.                           | `group.background = "#F0F0F0"`         |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "item_grid"
grid_size = { rows = 3, columns = 4 }
cell_size = "64px"
dynamic = true
loading_animation = "spin"
grouping = true
items = [
    { id = "1", image = "@assets/sword.png", tooltip = "Sword", background_color = "#FF5733" },
    { id = "2", image = "@assets/shield.png", tooltip = "Shield", background_color = "#33FF57" },
    { id = "3", image = "@assets/potion.png", tooltip = "Potion", background_color = "#3357FF" }
]
animations = { add = "fade-in", remove = "fade-out" }
```

---

### **Example GSS Implementation**
```toml
[item_grid]
grid.gap = "10px"
grid.background = "#333"

[cell]
border = "1px solid #FFF"
hover.effect = "glow"
selected.effect = "scale-up"
loading.animation = "spin"
background.color = "#FF5733"

[group]
border = "2px solid #CCC"
background = "#F0F0F0"
```

---

### **Advanced Considerations**
1. **Item Interaction**:
   - Support drag-and-drop for rearranging items.
   - Context menus for item-specific actions.

2. **Pagination**:
   - Include support for large grids that exceed the visible area.

3. **Dynamic Co-Chain Integration**:
   - Fetch item data dynamically, such as inventory updates from a co-chain.

4. **Custom Animations**:
   - Allow GSS designers to define unique animations for item interactions and loading effects.

5. **Enhanced Grouping**:
   - Provide detailed grouping with unique styles for each group (e.g., different borders, backgrounds).

---

### **Conclusion**
The Item Grid Widget offers a robust and interactive way to organize and manage items visually. With features like grouping, dynamic updates, custom animations, and accessibility, it caters to diverse use cases and ensures a seamless experience across input devices.

---

### **Slider Widget**

The Slider Widget is a versatile component for selecting values or ranges within a defined spectrum. It supports advanced interactivity, dynamic range updates, and input-specific behavior to enhance usability across devices.

---

### **Core Features**
1. **Single Value and Range Selection**:
   - Supports a single slider for choosing one value or a dual slider with multiple thumbs for defining ranges.

2. **Dynamic Ranges**:
   - Min and max values can be dynamically linked to external sources, such as UndChain locations.

3. **Custom Markers and Snapping**:
   - Allow custom markers or breaks on the slider track.
   - Enable snapping to predefined values for precision.

4. **Labels and Tooltips**:
   - Display current value(s) above the slider.
   - Optionally include labels for min, max, and intermediate values.

5. **Input-Specific Behavior**:
   - Tailored sensitivity and easing for controllers, keyboard arrow keys, mouse, and touch inputs.

6. **Visual, Audio, and Haptic Feedback**:
   - Optional audio cues for changes in value, such as clicks or tones.
   - Smooth animations for slider interactions, including entrance and exit effects.
   - Haptic feedback for compatible devices to enhance the tactile experience.

7. **Interactive Events**:
   - Events like `on_change`, `on_drag_start`, `on_drag_end`, `on_enter`, and `on_exit`.

8. **Accessibility**:
   - Fully keyboard and controller navigable.
   - Screen reader-friendly descriptions for values and labels.

---

### **Proposed Fields**
| **Field**          | **Description**                                                       | **Example**                               |
|--------------------|-----------------------------------------------------------------------|-------------------------------------------|
| `min`              | Minimum value for the slider.                                        | `min = 0`                                 |
| `max`              | Maximum value for the slider.                                        | `max = 100`                               |
| `step`             | Incremental step value for adjustments.                             | `step = 1`                                |
| `value`            | Current value of the slider (for single slider).                    | `value = 50`                              |
| `range`            | Current range values (for dual sliders).                            | `range = { start = 20, end = 80 }`        |
| `tooltip`          | Enables tooltips to display current value(s).                       | `tooltip = true`                          |
| `labels`           | Enables labels for min, max, and intermediate values.               | `labels = true`                           |
| `gradient_fill`    | Defines a color gradient for the slider track.                      | `gradient_fill = "linear-gradient(to right, #007BFF, #00FF00)"` |
| `markers`          | Predefined markers or breaks on the slider.                        | `markers = [0, 25, 50, 75, 100]`          |
| `snap_to_markers`  | Enables snapping to the nearest marker value.                       | `snap_to_markers = true`                  |
| `feedback`         | Feedback options including audio and haptics for interactions.       | `feedback = { audio = { change = "beep.wav" }, haptic = { intensity = "medium" } }` |
| `animations`       | Animations for slider interactions (e.g., entrance, exit, and thumb movement). | `animations = { entrance = "fade-in", exit = "fade-out", thumb_move = "ease-in-out" }` |

---

### **GSS Styling Parameters**
| **Parameter**            | **Description**                                                   | **Example**                              |
|--------------------------|-------------------------------------------------------------------|------------------------------------------|
| `slider.track.height`    | Height of the slider track.                                       | `slider.track.height = "6px"`          |
| `slider.track.color`     | Default color of the slider track.                               | `slider.track.color = "#CCC"`          |
| `slider.fill.color`      | Color of the filled portion of the slider.                       | `slider.fill.color = "#007BFF"`        |
| `slider.thumb.size`      | Size of the slider thumb.                                        | `slider.thumb.size = "16px"`           |
| `slider.thumb.color`     | Color of the slider thumb.                                       | `slider.thumb.color = "#FFF"`          |
| `slider.thumb.hover`     | Hover effect for the slider thumb.                              | `slider.thumb.hover = "glow"`          |
| `tooltip.background`     | Background color of the tooltip.                                | `tooltip.background = "#000"`          |
| `tooltip.font.color`     | Font color of the tooltip.                                       | `tooltip.font.color = "#FFF"`          |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "slider"
min = 0
max = 100
step = 1
value = 50
tooltip = true
labels = true
gradient_fill = "linear-gradient(to right, #007BFF, #00FF00)"
markers = [0, 25, 50, 75, 100]
snap_to_markers = true
feedback = { audio = { change = "beep.wav" }, haptic = { intensity = "medium" } }
animations = { entrance = "fade-in", exit = "fade-out", thumb_move = "ease-in-out" }
```

---

### **Example GSS Implementation**
```toml
[slider.track]
height = "6px"
color = "#CCC"
fill.color = "#007BFF"

[slider.thumb]
size = "16px"
color = "#FFF"
hover = "glow"

[tooltip]
background = "#000"
font.color = "#FFF"
```

---

### **Advanced Considerations**
1. **Dynamic Range Updates**:
   - Min and max values can update dynamically by linking to external sources, such as co-chains on UndChain.

2. **Dual Sliders with Multiple Thumbs**:
   - Support for two or more thumbs to define multiple ranges.

3. **Custom Markers and Snapping**:
   - Allow snapping to predefined markers for precise selection.

4. **Input-Specific Behavior**:
   - Easing curves for keyboard arrow keys, controllers, and touch interactions.

5. **Enhanced Animations**:
   - Entrance and exit animations for smoother transitions.
   - Dynamic animations for thumb movement and snapping.

6. **Haptic Feedback Integration**:
   - Provide tactile responses for interactions to enhance user experience on compatible devices.

---

### **Conclusion**
The Slider Widget is a highly customizable and interactive component for selecting values or ranges. With features like dynamic ranges, custom markers, snapping, enhanced animations, and feedback options (audio and haptics), it adapts seamlessly to various use cases while ensuring an engaging user experience across all input devices.

---

### **Progress Bar Widget**

The Progress Bar Widget visually represents progress toward a goal. It is customizable for various use cases, such as task completion, loading indicators, or milestone tracking, with support for animations, tooltips, and dynamic updates.

---

### **Core Features**
1. **Single or Multi-Step Progress**:
   - Supports continuous progress bars for single tasks.
   - Multi-step progress bars with defined milestones or stages.

2. **Customizable Range and Precision**:
   - Define the minimum and maximum values for the progress.
   - Supports precision for fractional progress updates.

3. **Dynamic Updates**:
   - Real-time updates to reflect progress changes.
   - Can integrate with external sources for dynamic progress tracking.

4. **Visual Indicators**:
   - Color-coded segments to represent different stages or statuses.
   - Optional gradient fills for smoother transitions.

5. **Labels and Tooltips**:
   - Display the current progress percentage or value directly on the bar.
   - Tooltips to show additional context for progress.

6. **Input-Specific Feedback**:
   - Includes visual, audio, and haptic feedback for updates and completions.

7. **Interactive Events**:
   - Events like `on_start`, `on_progress`, and `on_complete`.

8. **Accessibility**:
   - Screen reader-friendly descriptions for progress updates.
   - Fully navigable and understandable for users with disabilities.

---

### **Proposed Fields**
| **Field**          | **Description**                                                       | **Example**                               |
|--------------------|-----------------------------------------------------------------------|-------------------------------------------|
| `min`              | Minimum value of the progress bar.                                   | `min = 0`                                 |
| `max`              | Maximum value of the progress bar.                                   | `max = 100`                               |
| `value`            | Current progress value.                                              | `value = 50`                              |
| `segments`         | Defines segments for multi-step progress bars.                      | `segments = [25, 50, 75, 100]`            |
| `tooltip`          | Enables tooltips to display progress details.                       | `tooltip = true`                          |
| `gradient_fill`    | Defines a color gradient for the progress bar.                      | `gradient_fill = "linear-gradient(to right, #007BFF, #00FF00)"` |
| `feedback`         | Feedback options including audio and haptics for updates.            | `feedback = { audio = { progress = "tick.wav" }, haptic = { intensity = "low" } }` |
| `animations`       | Animations for progress updates and completion.                     | `animations = { update = "smooth", completion = "pulse" }` |

---

### **GSS Styling Parameters**
| **Parameter**            | **Description**                                                   | **Example**                              |
|--------------------------|-------------------------------------------------------------------|------------------------------------------|
| `progress.bar.height`    | Height of the progress bar.                                       | `progress.bar.height = "10px"`          |
| `progress.bar.color`     | Default color of the progress bar.                               | `progress.bar.color = "#CCC"`          |
| `progress.fill.color`    | Color of the filled portion of the progress bar.                 | `progress.fill.color = "#007BFF"`      |
| `progress.segment.color` | Color for individual segments in a multi-step progress bar.      | `progress.segment.color = "#00FF00"`   |
| `tooltip.background`     | Background color of the tooltip.                                | `tooltip.background = "#000"`          |
| `tooltip.font.color`     | Font color of the tooltip.                                       | `tooltip.font.color = "#FFF"`          |

---

### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "progress_bar"
min = 0
max = 100
value = 50
tooltip = true
gradient_fill = "linear-gradient(to right, #007BFF, #00FF00)"
segments = [25, 50, 75, 100]
feedback = { audio = { progress = "tick.wav" }, haptic = { intensity = "low" } }
animations = { update = "smooth", completion = "pulse" }
```

---

### **Example GSS Implementation**
```toml
[progress.bar]
height = "10px"
color = "#CCC"
fill.color = "#007BFF"

[progress.segment]
color = "#00FF00"

[tooltip]
background = "#000"
font.color = "#FFF"
```

---

### **Advanced Considerations**
1. **Real-Time Updates**:
   - Fetch progress data dynamically from external sources or co-chains.

2. **Custom Completion Effects**:
   - Allow developers to customize animations and feedback for completed progress bars.

3. **Multi-Device Feedback**:
   - Provide consistent feedback across devices, including haptic responses on mobile and controller inputs.

4. **Segmented Progress Bars**:
   - Highlight milestones or stages within the progress bar.
   - Allow unique styles and effects for each segment.

---

### **Conclusion**
The Progress Bar Widget offers a customizable and dynamic way to visualize progress. With features like real-time updates, segmented progress, and feedback options (audio, visual, and haptics), it provides an engaging and accessible experience for diverse applications and devices.

---

## Summary

This appendix showcases the flexibility and modularity of M3L and GSS through a comprehensive widget catalog. Developers can use these examples to create visually consistent and functional applications while ensuring compatibility with future enhancements.