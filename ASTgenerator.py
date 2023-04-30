class ASTNode:
    def visit(self, visitor):
        pass

class VarDeclNode(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def visit(self, visitor):
        return visitor.visit_var_decl(self)

class OpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def visit(self, visitor):
        return visitor.visit_op(self)

class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

    def visit(self, visitor):
        return visitor.visit_print(self)

import ast

class ASTGenerator(ast.NodeVisitor):
    def visit_Assign(self, node):
        var_name = node.targets[0].id
        var_value = self.visit(node.value)
        return VarDeclNode(var_name, var_value)

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        op = node.op.__class__.__name__
        right = self.visit(node.right)
        return OpNode(left, op, right)

    def visit_Num(self, node):
        return node.n

    def visit_Print(self, node):
        expr = self.visit(node.values[0])
        return PrintNode(expr)

    def generic_visit(self, node):
        raise Exception(f"Unsupported node type: {type(node).__name__}")

def generate_ast(source_code):
    tree = ast.parse(source_code)
    generator = ASTGenerator()
    return generator.visit(tree)


source_code = """
x = 1 + 2
print(x)
"""

ast_root = generate_ast(source_code)
print(ast_root.visit(ASTPrinter())) # ASTPrinter is a Visitor class to print the AST

