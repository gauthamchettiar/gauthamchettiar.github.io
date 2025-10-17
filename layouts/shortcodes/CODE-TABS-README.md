# Code Tabs Shortcode

A CSS-only tabbed code fence shortcode for Hugo. No JavaScript required!

## Features

- Pure CSS implementation using radio buttons
- Syntax highlighting support
- Dark mode compatible
- Responsive design
- Multiple code blocks with language tabs

## Usage

Use the `code-tabs` shortcode with a comma-separated list of language names:

```markdown
{{< code-tabs "Python,JavaScript,Go" >}}
```python
print("Hello World")
```
|||
```javascript
console.log("Hello World");
```
|||
```go
fmt.Println("Hello World")
```
{{< /code-tabs >}}
```

## Syntax

1. **Opening tag**: `{{< code-tabs "Lang1,Lang2,Lang3" >}}`
   - First parameter is a comma-separated list of language names (will be displayed as tab labels)

2. **Code blocks**: Separate each code block with `|||`
   - Use standard markdown code fences with language identifier
   - Number of code blocks should match number of languages in the parameter

3. **Closing tag**: `{{< /code-tabs >}}`

## How It Works

The shortcode uses:
- Hidden radio inputs to track which tab is selected
- CSS `:checked` pseudo-selector to show/hide content
- CSS sibling combinators (`+` and `~`) to style tabs and content
- Unique IDs per instance to avoid conflicts when multiple shortcodes are on the same page

## Styling

The shortcode includes:
- Hover effects on tabs
- Active tab highlighting
- Dark mode support (via `@media (prefers-color-scheme: dark)`)
- Smooth transitions

You can customize colors by modifying the CSS variables:
- `var(--background-color)` - Used for active tab background
- `var(--heading-color)` - Used for active tab text and border

## Example

See `content/blog/code-tabs-demo.md` for a working example.
