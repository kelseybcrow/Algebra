
# TODO: EXAM1_CAREFUL_USE_CALCULATOR_FOR_ALL_PEMDAS_OPERATIONS
' ➜  do not ever do mental math, too risky for small errors '
# ➜  always use the calcualtor for multiplying, dividing, adding, etc...

'''
Next problem:
➜ Find the domain & range of the graphed function g using interval notation:
'''

# TODO: EXAM_DOMAIN_RANGE_GRAPHED_FUNCTION_INTERVAL_NOTATION

# graph starts horizontally at x = (-4) with a closed circle, so (-4) is included ➜
# graph ends horizontally at x = 5 with an open circle, so 4 is not included ➜
    function_domain = [(-4), 4)

# graph starts vertically at (-5) with open circle, so (-5) is not included ➜
# graph ends vertically at 3 with closed circle, so 3 is included
    function_range = ((-5), 3]

'''
Next problem:
➜ Find the solution for u ~ two fractions with binomials equaling each other
'''
    5 / (u + 3)   =   [5 / (3u + 9)] + (-2)

# TODO: EXAM_FRACTIONS_MULTIPLYING_SUBSTITUTION_WITH_FACTORING

# instead of dealing with fractions right away, look at the equation structure

# notice that the block ➜
    5 / (u + 3)
# appears on both sides of the equation

# create a variable called factor to represent that block ➜
    factor = 5 / (u + 3)

# plug factor back into the equation in place of: 5 / (u + 3) ➜
    factor = (1/3)factor + (-2)

# TODO: EXAM_FRACTIONS_MULTIPLYING_REVEAL_THE_HIDDEN_1*n

# revealing the hidden "1 * ()" works for both numerators and denominators

# reveal the hidden 1 being multiplied by 5 on the top and reveal the hidden (*) symbol between the 3 and the binomial (u + 3) ➜
    1 * 5
━━━━━━━
  3 * (u + 3)
# the same as ➜ ➜ ➜
    1             5
━━━━━  *  ━━━━━
    3           (u + 3)
# now that the fraction is split into its factors, substitute the factor back into the equation ➜
                1
factor  =   ━━━━━ factor + (-2)
                3

# move the ➜
    (1/3)factor
# to the left side of the equation by subtracting it from both sides

# TODO: EXAM_FRACTIONS_MULTIPLYING_REVEAL_HIDDEN_(1=n/n)

# reveal the hidden (3/3) in front of factor on the left side of the equation ➜
    (3/3)factor + [-(1/3)factor]   =   (-2)
      ➜  (3/3) + (-1/3) = (2/3)  ➜
      (2/3)factor   =   (-2)
# to isolate factor, multiply both sides by the reciprocal (3/2)
    (3/2) * (2/3)factor   =   (3/2) * (-2)

# TODO: EXAM_FRACTIONS_MULTIPLYING_USING_EQUIVALENT_FRACTIONS
# ➜ rewrite (-2) as (-4/2)
    (3/2) * (2/3)factor   =   (3/2) * (-4/2)

    ➜  (3/2) and (2/3) cancel out
    ➜  numerators 3 * (-4) = (-12)
    ➜  denominators 2 * 2 = 4

    factor = (-12) / 4
    factor = (-3)

# now set the value of factor equal to its definition ➜
    (-3) = 5 / (u + 3)

# clear the fraction by multiplying both sides by (u + 3)
    (u + 3)*[(-3)]   =   (u + 3)*[5 / (u + 3)]

# for the right side, reveal the hidden 1 ➜
        u + 3         5
      ━━━━━ * ━━━━━
          1         u + 3
# the top and bottom (u + 3) cancel out, leaving only the 5 numerator
    (-3)(u + 3)   =   5

# distribute the (-3) on the left side
    (-3u) + (-9)   =   5

# add 9 on both sides
    (-3u) + (-9)   =   5
      + 9   =   + 9
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    (-3u)   =   14

# divide both sides by (-3)
    (-3u)   =   14
      / (-3)   =   / (-3)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    [u = (-14/3)]

# TODO: EXAM_CLEAR_FRACTIONS_BY_LCD
" ➜  3 step shortcut to dissolve fractions in an equation"
    " ➜  find the LCD of the whole equation"
    " ➜  multiply every single term by that LCD immediately"
    " ➜  watch the fractions dissappear"
'''
The same problem but done the LCD way:
➜ Find the solution for u ~ two fractions with binomials equaling each other
'''
    5 / (u + 3)   =   [5 / (3u + 9)] + (-2)

# denominators are: (u + 3) and 3(u + 3)
# find the LCD by factoring the larger denominator ➜
    3u + 9 =
    3(u + 3)
    LCD = 3(u + 3)

# TODO: EXAM_LCD_RULE
" ➜  LCD is the smallest possible container in which all denominators must fit inside"
    (u + 3) fits inside 3(u + 3)
    3(u + 3) also fits inside 3(u + 3)

# multiply every single term by the LCD ➜ 3(u + 3)
    3(u + 3)*[5 / (u + 3)]   =   3(u + 3)*[5 / 3(u + 3)]  + 3(u + 3)*[-2]

# TODO: EXAM_USING_VARIABLES_LEFT_RIGHT_SIDE_EQUATION
 " ➜  the left_side and right_side variables make solving the equation in increments much easier to track ➜ "

# on the left side, the (u + 3)'s in both the numerator and denominator cancel each other out, so now we're left with ➜
    left_side = 3 * 5
    left_side = 15

# now for the right side ➜ in the first term, both 3(u + 3)'s cancel out ➜
    right_side = 5   +   3(u + 3)*[-2]

# TODO: EXAM_PEMDAS_ORDER_OF_OPERATIONS
" ➜  parentheses, exponents, multiplying, dividing, adding, subtracting ➜ "
" ➜  multiply the two plain outside numbers first ➜ it's a shortcut to turn two messy steps into one clean step ➜ "
    right_side = 5   +   3(u + 3)*[-2]
      3 * (-2) = (-6)
    right_side = 5   +   (-6)(u + 3)

# now distribute the (-6) ➜
    right_side = 5 + (-6u) + (-18)
    right_side = (-6u) + (-13)

# now set both sides equal to each other ➜
    left_side = 15
    right_side = (-6u) + (-13)

    15   =   (-6u) + (-13)
      + 13   =   + 13
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    28   =   (-6u)
      / (-6)   =   / (-6)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    (-28/6) = u

    [(-14/3) = u]

'''
Next problem:
➜ Find the simplification of radicals
'''
    √‾‾‾20w⁹y⁴ √‾‾‾5w³y²

# TODO: EXAM1_RADICALS_PERFECT_SQUARES
'➜  always look for the opportunity to use perfect squares when approaching radicals'

# while neither 20 or 5 are perfect squares on their own ➜ their product (20 * 5 = 100) is a perfect square!
    √‾‾‾20w⁹y⁴ √‾‾‾5w³y²

# combine under one radical ➜
    √‾‾‾20w⁹y⁴5w³y²

# multiply coefficients & add all the variables' exponents together ➜
    [coef] 20 * 5 = [100]
    [w] 9 + 3 = [12]
    [y] 4 + 2 = [6]

    √‾‾‾100w¹²y⁶

# TODO: EXAM1_SQUARE_ROOTS_OF_EXPONENTS_DIVIDE_BY_2
' ➜ divide the exponents by 2 when taking the square root of them '

# take the sqrt of each term to remove the radical ➜
    [coef] √‾‾‾100 = [10]
    [w] 12 ÷ 2 = [6]
    [y] 6 ÷ 2 = [3]

# solution with NO radical ➜
    [10w⁶y³]

'''
Next problem:
➜ Find w in a quadratic equation
'''
    5w²   =   14w + 3

# move all terms to the right side ➜
    5w²   =   14w + 3
      (-5w²)   =   (-5w²)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    0   =   (-5w²) + 14w + 3

    a = (-5)
    b = 14
    c = 3

# use the quadratic formula ➜
# TODO: EXAM1_QUADRATIC_FORMULA

    w  =  (-b) ± √‾‾[b² + (-4)ac]
    #━━━━━━━━━━━━━━━━━━━━━━━━━━
               2a
    a = (-5)
    b = 14
    c = 3

# TODO: EXAM1_CAREFUL_4_AND_a_LOOK_SIMILAR
' ➜ the 4/a similarity is especially tricky when using quadratic formulas ➜'

    w  =  (-14) ± √‾‾[14² + (-4)(-5)3]
    #━━━━━━━━━━━━━━━━━━━━━━━━━━
               2(-5)
    14² = 196
    (-4) * (-5) * 3 = 60
    196 + 60 = 256

    2 * (-5) = (-10)

    w  =  (-14) ± √‾‾[256]
         #━━━━━━━━━━━━━━━━━━━━━━━━━━
                    (-10)

    √‾‾‾[256] = 16

    w  =  (-14) + 16
         #━━━━━━━━━━━━━
              (-10)

" split into [+][-] cases: "
" [+] case ➜ "

    w  =  (-14) + 16
         #━━━━━━━━━━━━━
              (-10)

    [w = (-1/5)]

# perfect example of saving time and reducing the risk of error by plugging this whole thing into a calculator ➜ using parentheses for order of operations

" [-] case ➜ "

    w  =  (-14) + (-16)
         #━━━━━━━━━━━━━
              (-10)

# plug into calculator ➜
    w = 3

# final solution ➜
    [w = (-1/5), 3]

# TODO: EXAM1_CAREFUL_INPUT_PARENTHESES_FIRST_INTO_CALCULATOR_THEN_FILL_IN_VALUES
' ➜ helps reduce the risk of incorrectly defining the order of operations for the calculator and therefore trigging a wrong answer '

# solving this problem via factoring would have been slower because ➜

" when the leading coefficient is not 1 ➜ factoring requires a tedious process of factoring by grouping ➜ [the ac method] "

# TODO: EXAM1_QUADRATIC_USING_FACTORING_TO_SOLVE_THE_AC_METHOD
" ➜ the ac method ➜ "
# find a =  , b =  , c =
# multiply a * c to get target_number
# find 2 numbers where num_1 * num_2 = target_number AND num_1 + num_2 = b
# split the middle term
# group into pairs
# factor each pair by extracting the GCF
# group the factors into binomials
# set each binomial factor equal to zero
# solve both mini-equations


