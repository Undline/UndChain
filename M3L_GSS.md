
### **Documentation Structure for M3L and GSS**

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
- **Checkbox**: For binary selections.
- **Radio Button**: Allows a single selection from multiple options.
- **Switch**: For toggling states (e.g., on/off).
- **Input Box (Text Bar)**: Similar to a text box but styled for search or form input.
- **Scroll Area**: Indicates additional content is available via scroll or pan.
- **Text Area**: Multi-line input for larger text blocks.
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

### **Text Box**
- **Description**: A text box allows users to input single-line text. This widget supports rich interactivity and validation through events and intents.
- **Use Cases**:
  - Collecting user input (e.g., usernames, emails).
  - Real-time validation (e.g., regex, min/max length).
  - Dynamic interactions (e.g., triggering co-chain requests).

---

#### **Core Fields**
| Field       | Description                                                                 | Example                                                                                                                                       |
|-------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| `label`     | A descriptive title or prompt for the text box. Rendered via GSS styling.  | `label = "Enter Username"`                                                                                                                  |
| `placeholder`| Text displayed inside the box when it is empty.                           | `placeholder = "Enter your username"`                                                                                                       |
| `on_input`  | Triggers actions as the user types.                                         | `on_input = [{ validate = "regex", pattern = "^[a-zA-Z0-9_]+$" }, { after_idle = "2s", intent = "check_availability", target = "UndChain://UnaS/namecheck" }]` |
| `on_exit`   | Triggers actions when the user leaves the text box.                        | `on_exit = [{ validate = "regex", pattern = "^[^@\s]+@[^@\s]+\.[^@\s]+$" }]`                                                        |
| `on_enter`  | Fires when the text box gains focus.                                        | `on_enter = [{ show_help = "Enter a unique username." }]`                                                                                   |
| `on_next`   | Handles navigation to the next widget in the flow.                         | `on_next = "password_field"`                                                                                                                |
| `on_submit` | Fires when the user confirms input (e.g., pressing Enter).                 | `on_submit = [{ validate = "min_length", value = 3 }, { intent = "search", target = "SQeeL://Auction_House/search" }]`                  |
| `on_error`  | Triggers actions when an error specific to the widget occurs.              | `on_error = [{ display = "tooltip", message = "This field is required." }]`                                                               |

---

#### **Example M3L Implementation**
```toml
[[layout.container.content]]
type = "text_box"
label = "Username"
placeholder = "Enter your username"
on_input = [
    { validate = "no_special_chars", error_message = "Special characters are not allowed." },
    { min_length = 3, error_message = "Must be at least 3 characters." },
    { after_idle = "2s", intent = "check_availability", target = "UndChain://UnaS/namecheck", error_message = "Username is unavailable." }
]
on_exit = [
    { validate = "regex", pattern = "^[a-zA-Z0-9_]+$", error_message = "Only alphanumeric characters allowed." }
]
on_next = "password_field"
on_error = [
    { display = "tooltip", message = "This field is required." }
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

[text_box.label]
font-size = "1rem"
color = "#666"
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

[text_box.error.tooltip]
background-color = "#FFDDDD"
color = "#FF0000"
padding = "0.25rem"
border-radius = "3px"
```

---

### **Key Features and Recommendations**
- **Rich Event Handling**: Leverage `on_input`, `on_exit`, `on_enter`, `on_next`, `on_submit`, and `on_error` for dynamic interactions and seamless user experiences.
- **Validation Options**: Support for client-side and co-chain validation ensures flexibility and scalability.
- **Dynamic Feedback**: Integrate GSS rules for valid, invalid, and waiting states to provide real-time feedback.
- **Accessibility**: Use ARIA roles and descriptions to enhance usability for assistive technologies.

---

### **Additional Recommendations for Flexibility**
1. **Custom Error Messages**: Allow developers to specify tailored messages for validation failures.
2. **Dynamic Placeholders**: Fetch placeholder text dynamically via co-chains for context-aware prompts.
3. **Prefilled Values**: Add a `default_value` field to initialize the text box with preset data.
4. **Event Throttling**: Introduce a `throttle` option to limit rapid event triggering (e.g., `throttle = "500ms"`).

---

## Summary

This appendix showcases the flexibility and modularity of M3L and GSS through a comprehensive widget catalog. Developers can use these examples to create visually consistent and functional applications while ensuring compatibility with future enhancements.